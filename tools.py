"""Tool definitions and implementations for GenericAgent.

This module provides the built-in tools available to the agent,
including web browsing, code execution, file I/O, and search.
Each tool follows the OpenAI function-calling schema.
"""

import os
import subprocess
import json
from typing import Any


# ---------------------------------------------------------------------------
# Tool schema definitions (mirrored in tools_schema.json for the LLM)
# ---------------------------------------------------------------------------

TOOL_REGISTRY: dict[str, callable] = {}


def register_tool(name: str):
    """Decorator that registers a callable under *name* in TOOL_REGISTRY."""
    def decorator(fn):
        TOOL_REGISTRY[name] = fn
        return fn
    return decorator


# ---------------------------------------------------------------------------
# Shell / code execution
# ---------------------------------------------------------------------------

@register_tool("run_shell")
def run_shell(command: str, timeout: int = 30) -> dict[str, Any]:
    """Execute a shell command and return stdout/stderr.

    Args:
        command: The shell command to run.
        timeout: Maximum seconds to wait before killing the process.

    Returns:
        A dict with keys ``stdout``, ``stderr``, and ``returncode``.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": f"Command timed out after {timeout}s", "returncode": -1}
    except Exception as exc:  # noqa: BLE001
        return {"stdout": "", "stderr": str(exc), "returncode": -1}


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

@register_tool("read_file")
def read_file(path: str) -> dict[str, Any]:
    """Read the contents of a file.

    Args:
        path: Absolute or relative path to the file.

    Returns:
        A dict with key ``content`` on success, or ``error`` on failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return {"content": fh.read()}
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


@register_tool("write_file")
def write_file(path: str, content: str, append: bool = False) -> dict[str, Any]:
    """Write (or append) text to a file, creating it if necessary.

    Args:
        path: Destination file path.
        content: Text to write.
        append: If True, append rather than overwrite.

    Returns:
        A dict with key ``bytes_written`` on success, or ``error`` on failure.
    """
    mode = "a" if append else "w"
    try:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, mode, encoding="utf-8") as fh:
            fh.write(content)
        return {"bytes_written": len(content.encode())}
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# JSON helper (useful for structured data)
# ---------------------------------------------------------------------------

@register_tool("parse_json")
def parse_json(text: str) -> dict[str, Any]:
    """Parse a JSON string and return the resulting object.

    Args:
        text: A JSON-encoded string.

    Returns:
        The parsed object, or a dict with key ``error`` if parsing fails.
    """
    try:
        return {"result": json.loads(text)}
    except json.JSONDecodeError as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Dispatch helper used by agent_loop
# ---------------------------------------------------------------------------

def dispatch_tool(name: str, arguments: dict[str, Any]) -> Any:
    """Look up *name* in TOOL_REGISTRY and call it with *arguments*.

    Args:
        name: Registered tool name.
        arguments: Keyword arguments forwarded to the tool function.

    Returns:
        The tool's return value, or an error dict if the tool is unknown.
    """
    fn = TOOL_REGISTRY.get(name)
    if fn is None:
        return {"error": f"Unknown tool: '{name}'. Available: {list(TOOL_REGISTRY)}"}
    return fn(**arguments)
