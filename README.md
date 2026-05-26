<div align="center">

<img src="assets/images/bar.jpg" width="880" alt="GenericAgent Banner"/>

# GenericAgent

**A Minimal, Self-Evolving Autonomous Agent Framework**

*~3K lines of seed code · 9 atomic tools · ~100-line Agent Loop*

<p>

  <a href="https://arxiv.org/abs/2604.17091"><img src="https://img.shields.io/badge/Technical_Report-PDF-EA4335?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="Technical Report"/></a>
  <a href="https://github.com/JinyiHan99/GA-Technical-Report"><img src="https://img.shields.io/badge/Code_%26_Data-Reproduction-181717?style=flat-square&logo=github" alt="Reproduction Repo"/></a>
  <a href="https://datawhalechina.github.io/hello-generic-agent/"><img src="https://img.shields.io/badge/Tutorial-Datawhale-blue?style=flat-square" alt="Tutorial"/></a>
  <a href="https://fudankw.cn/sophub"><img src="https://img.shields.io/badge/Skill_Hub-Sophub-purple?style=flat-square" alt="Sophub"/></a>
</p>

<p>
  <a href="https://trendshift.io/repositories/25944" target="_blank"><img src="https://trendshift.io/api/badge/repositories/25944" alt="Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

**[English](#-english) · [中文](#-中文)**

</div>

> 📌 **Official Channel** — This GitHub repository is the **only** official source of GenericAgent.
> We have no affiliation with any third-party website using the GenericAgent name.

> 📝 **Personal Fork Note** — I'm using this fork to experiment with GenericAgent on my own machine.
> Running it with the `gpt-4o` model and testing skill accumulation on file management tasks.

---

<a id="-english"></a>

## 🌟 Overview

**GenericAgent** is a minimal, self-evolving autonomous agent framework. Its core is just **~3K lines of code**. Through **9 atomic tools + a ~100-line Agent Loop**, it grants any LLM system-level control over a local computer — covering browser, terminal, filesystem, keyboard/mouse input, screen vision, and mobile devices (ADB).

> Design philosophy — **don't preload skills, evolve them.**

Every time GenericAgent solves a new task, it automatically crystallizes the execution path into a reusable **Skill**. The longer you use it, the more skills accumulate — forming a personal skill tree grown entirely from 3K lines of seed code.

> 🤖 **Self-Bootstrap Proof** — Everything in this repository, from installing Git and running `git init` to every commit message, was completed autonomously by GenericAgent. The author never opened a terminal once.

### 📑 Table of Contents

- [Key Features](#-key-features)
- [Demo Showcase](#-demo-showcase)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Self-Evolution Mechanism](#-self-evolution-mechanism)
- [Comparison](#-comparison)
- [Evaluation](#-evaluation)
- [Roadmap & News](#-roadmap--news)
- [Community & Support](#-community--support)
- [License](#-license)

---

## 📋 Key Features

| Feature | Description |
| :--- | :--- |
| 🧬 **Self-Evolving** | Automatically crystallizes each task into a Skill. Capabilities grow with every use, forming your personal skill tree. |
| 🪶 **Minimal Architecture** | ~3K lines of core code. Agent Loop is ~100 lines. No compl
