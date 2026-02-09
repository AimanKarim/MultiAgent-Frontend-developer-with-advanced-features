# 🚀 AI Frontend Multi-Agent System

An autonomous multi-agent pipeline that converts a **plain English product idea** into:

✅ structured requirements
✅ a UI design mockup
✅ production-ready HTML & CSS
✅ automated QA validation

Powered by **CrewAI + Gemini 2.5 Flash**.

---

## 🧠 How It Works

The system simulates a real product team.

```
User → Requirements Agent → Design Agent → Gemini (Frontend Dev) → QA Agent
```

1. **Requirements Agent**
   Extracts structured intent from natural language.

2. **Design Agent**
   Creates visual direction + generates a mockup prompt.

3. **Gemini 2.5 Flash**
   Reads the mockup and writes real HTML & CSS.

4. **QA Agent**
   Validates structure, styling, and completeness.

---

## ✨ Features

* 🧩 Modular multi-agent architecture
* 🎨 AI-generated UI mockups
* 💻 Automatic HTML & CSS generation
* 🔍 Built-in quality checks
* 🔄 Domain agnostic (works for any business)
* ⚡ Uses Gemini 2.5 Flash for fast generation

---

## 📂 Project Structure

```
.
├── agents/
│   ├── requirements_agent.py
│   ├── design_agent.py
│   └── qa_agent.py
│
├── tools/
│   ├── image_tool.py
│   └── file_writer.py
│
├── outputs/
│   ├── designs/
│   └── code/
│
├── llm.py
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone repo

```bash
git clone https://github.com/yourusername/ai-frontend-agents.git
cd ai-frontend-agents
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
# windows
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install crewai google-generativeai pillow
```

---

## 🔑 Setup API Key

```bash
export GEMINI_API_KEY="your_key_here"
# windows
set GEMINI_API_KEY=your_key_here
```

---

## ▶️ Run

```bash
python main.py
```

Example input:

```
Modern coffee shop landing page, warm brown colors, cozy, minimal.
```

---

## 📦 Output (automatically generated)

### Mockup

```
outputs/designs/mockup.png
```

### Generated Code

```
outputs/code/index.html
outputs/code/style.css
```

---

## 🧪 QA Checks

The QA agent verifies:

* CSS file is linked
* CSS is not empty
* Semantic sections exist

---

## 🧨 Why This Is Cool

This is essentially:

👉 an AI product team
👉 automated designer + developer
👉 instant UI prototyping
👉 no human writing code

Great for:

* MVP generation
* rapid experimentation
* internal tooling
* design → code automation
