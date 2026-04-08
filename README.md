# 🧠 Multi-Agent System with LangGraph + Modal + DeepAgents

## 🚀 Overview

This project implements a **local multi-agent system** using LangGraph for orchestration, Modal for secure sandboxed execution, and DeepAgents (hybrid usage) for intelligent tool invocation.

It demonstrates how to build a **modular, extensible agent architecture** with:

* 📄 PDF Question Answering (with citations)
* 💻 Safe shell command execution (Modal + DeepAgents)
* 🧩 Skill-based design
* 🔀 Multi-agent routing
* 🧠 Conversational memory

> ⚠️ Modal setup is required for command execution features.

---

## 🏗️ Architecture

```text
User Input
    ↓
Router (LLM + Rules)
    ↓
 ┌───────────────┬──────────────────────┬───────────────┐
 │               │                      │
PDF Agent     Command Agent        Unknown Agent
 │               │                      │
PDF Skill     Command Skill        Fallback
 │               │
Vector DB     DeepAgent Wrapper
                 ↓
              Tool Layer
                 ↓
              Modal Sandbox
```

---

## 🧩 Core Features

### 📄 PDF Question Answering (RAG)

* Loads and chunks PDF documents
* Stores embeddings in FAISS vector database
* Retrieves relevant chunks based on query
* Returns **grounded answers with page citations**

Example:

```text
Artificial intelligence is defined as... (Page 2, Page 5)
```

---

### 💻 Sandboxed Command Execution

* Executes shell commands via Modal sandbox
* Uses DeepAgents for tool selection
* Enforces tool usage with strict prompts
* Example:

```bash
run: echo hello world
```

---

### 🔀 Multi-Agent Routing

* Hybrid routing strategy:

  * Rule-based (fast & deterministic)
  * LLM-based (flexible)
* Routes tasks to:

  * `pdf_agent`
  * `command_agent`
  * `unknown_agent`

---

### 🧩 Skills System

* Encapsulates capabilities as reusable **skills**
* Agents invoke skills dynamically
* Keeps architecture modular and extensible

---

### 🧠 Conversational Memory

* Maintains structured message history
* Supports follow-up questions
* Improves contextual understanding

---

## ⚙️ Tech Stack

* LangGraph → Agent orchestration
* LangChain → LLM + tools
* OpenAI API → Language model
* Modal → Sandboxed execution
* FAISS → Vector similarity search
* DeepAgents → Tool invocation (command agent only)

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ☁️ Modal Setup (Required)

This project uses Modal to execute shell commands in a secure sandbox environment.

### 1. Install Modal CLI

```bash
pip install modal
```

---

### 2. Authenticate

```bash
modal setup
```

---

### 3. Verify

```bash
modal token new
```

---

### ⚠️ Notes

* Required for command execution
* PDF Q&A works without Modal

---

## ▶️ Run the Project

```bash
# Recommended (full features)
modal run main.py

# Local run (no command execution)
python main.py
```

---

## 🧪 Example Usage

```text
🧑 User: What is this PDF about?
🤖 Assistant: The document discusses occupational diseases... (Page 2, Page 11)

🧑 User: Explain more
🤖 Assistant: It further describes...

🧑 User: run: echo hello
🤖 Assistant: hello

🧑 User: tell me a joke
🤖 Assistant: Sorry, I cannot handle this request.
```

---

## 🧠 Key Design Decisions

### 1. Skill-Based Architecture

* Clear separation of concerns
* Agent = orchestration
* Skill = execution
* Tool = low-level action

---

### 2. Hybrid Routing Strategy

* Rule-based for reliability
* LLM-based for flexibility
* Fallback for unknown tasks

---

### 3. Metadata-Aware RAG

* Stores page numbers in vector DB
* Enables inline citations
* Ensures grounded responses

---

### 4. DeepAgents (Hybrid Usage)

* Used **only for command agent**
* Handles tool invocation via LLM
* Enforced with strict system prompts
* Fallback ensures deterministic execution

---

### 5. Modal Sandbox

* Secure isolated execution
* Prevents unsafe system access
* Clean integration with tool layer

---

### 6. Structured Memory

* Message-based history
* Supports multi-turn interactions
* Aligns with LangChain/LangGraph design

---

## ❌ Not Implemented (By Design)

* Multi-step planning (kept simple intentionally)
* Full DeepAgents system (used partially only)
* UI layer (CLI-based)

👉 Focus: **clarity, control, maintainability**

---

## 🚀 Future Improvements

* 🌐 Web search skill
* 🎨 UI (Streamlit / React)
* ⚡ Streaming responses
* 📂 File upload support
* 🧠 Long-term memory

---

## 🎯 What This Project Demonstrates

* Multi-agent system design
* Retrieval-Augmented Generation (RAG)
* Safe tool execution
* Hybrid AI architecture (manual + DeepAgents)
* Stateful conversations

---

## 👤 Author

**Chau Nguyen**

---

## 💡 Inspiration

Inspired by modern agent architectures:

* LangGraph
* DeepAgents

This project **reimplements core ideas manually** to:

* improve understanding
* maintain control
* ensure reliability
