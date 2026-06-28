![Python](https://img.shields.io/badge/Python-3.10-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Llama](https://img.shields.io/badge/Model-Llama_3.1_8b_instant-green)
![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)
![AI Agents](https://img.shields.io/badge/AI-Agent_Tool_Calling-red)
![DuckDuckGo](https://img.shields.io/badge/Search-DuckDuckGo-yellow)
![BeautifulSoup](https://img.shields.io/badge/Web_Scraping-BeautifulSoup-green)
![Markdown](https://img.shields.io/badge/Output-Markdown_Report-orange)

# 🔍 AI Research Assistant

An AI-powered **Research Assistant** built using **Groq API**, **Llama 3.3**, and **LangChain** that autonomously researches topics by searching the web, reading webpages, and generating structured research reports using **tool-calling AI agents**.

Instead of answering solely from the LLM's knowledge, the agent dynamically decides when to use external tools, retrieves up-to-date information from the web, and synthesizes information into professional markdown reports.

This project demonstrates the fundamentals of **AI Agents**, **Tool Calling**, **LLM Orchestration**, **Prompt Engineering**, and **Web-Augmented Generation**.

---

# 🚀 Features

* 🔎 AI Agent with Tool Calling
* 🌐 DuckDuckGo Web Search Integration
* 📄 Automatic Webpage Reading
* 🧹 HTML Content Extraction using BeautifulSoup
* 🤖 Groq + Llama 3.3 Integration
* 🧠 Prompt Engineering
* 🔄 Multi-Step Agent Reasoning Loop
* 📑 Professional Markdown Report Generation
* 📂 Automatic Report Saving
* ⚡ Ultra-fast Inference using Groq
* 🔐 Secure API Key Management using Environment Variables
* 🏗️ Modular Production-Style Project Structure

---

# 🏗️ Architecture

```text
                    User Query
                         │
                         ▼
                Llama 3.3 (Groq)
                         │
             Determines Required Tool
                         │
        ┌────────────────┴─────────────────┐
        ▼                                  ▼
 DuckDuckGo Search Tool             Read Webpage Tool
        │                                  │
        └────────────────┬─────────────────┘
                         ▼
                 Tool Execution
                         │
                         ▼
                 Tool Observations
                         │
                         ▼
              LLM Reasoning Loop
                         │
                         ▼
          Professional Research Report
                         │
                         ▼
           Markdown File (.md)
```

---

# 📂 Project Structure

```text
research-assistant/
│
├── app.py                  # Entry point
├── agent.py                # Agent reasoning loop
├── llm.py                  # Groq model configuration
├── prompts.py              # Prompt templates
├── tools.py                # AI tools
│
├── utils/
│   ├── scraper.py          # Webpage reader
│   └── report.py           # Markdown report generator
│
├── outputs/                # Generated reports
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

| Component             | Technology               |
| --------------------- | ------------------------ |
| Language              | Python                   |
| LLM Provider          | Groq API                 |
| Model                 | Llama 3.3 70B Versatile  |
| Framework             | LangChain                |
| Agent Pattern         | Tool Calling             |
| Search Engine         | DuckDuckGo               |
| Web Scraping          | BeautifulSoup + Requests |
| Output                | Markdown Report          |
| Environment Variables | python-dotenv            |

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/research-assistant.git

cd research-assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Project

```bash
python app.py
```

Example:

```text
Research Topic:

AI Agents
```

The application automatically:

* Searches the web
* Reads relevant webpages
* Extracts useful content
* Performs multi-step reasoning
* Generates a professional markdown research report

---

# 💡 How It Works

1. User enters a research topic.
2. The LLM determines whether external knowledge is required.
3. The AI agent calls the Web Search tool.
4. Search results are returned.
5. The AI agent decides which webpages to read.
6. HTML content is cleaned and converted into plain text.
7. Tool observations are returned to the LLM.
8. The reasoning loop continues until sufficient information has been gathered.
9. The LLM generates a structured research report.
10. The report is saved as a Markdown file.

---

# 🧠 Key Concepts Learned

### 🤖 AI Agents

Building autonomous LLM applications capable of reasoning and interacting with external tools.

### 🔧 Tool Calling

Allowing LLMs to dynamically decide which tools to invoke during problem solving.

### 🔄 Agent Reasoning Loop

Implementing iterative reasoning using the cycle:

Think → Tool → Observation → Think → Answer

### 🌐 Web-Augmented Generation

Combining real-time web search with LLM reasoning to produce current and factual responses.

### 🧹 HTML Parsing

Extracting clean textual content from webpages using BeautifulSoup.

### 🧠 Prompt Engineering

Designing prompts that guide the LLM to generate structured, high-quality research reports.

### 📑 Markdown Report Generation

Automatically exporting research findings into reusable Markdown documents.

### 🏗️ Modular AI Application Design

Separating the application into independent modules for tools, prompts, agent logic, LLM configuration, and utilities.

---

# 🚀 Future Improvements

* 🧠 Multi-Agent Research System
* 📚 Tavily Search Integration
* 📄 PDF Export
* 📑 DOCX Export
* 🎯 Research Planning Agent
* 🧠 Memory for Previous Research
* 🌍 Multi-language Support
* 📈 Research Quality Evaluation
* ⚡ Streaming Responses
* ☁️ FastAPI REST API
* 🐳 Docker Support
* ☁️ Cloud Deployment (Render / AWS)

---

# ⚠️ Limitations

* Webpages may block scraping.
* Research quality depends on publicly available information.
* No persistent memory between sessions.
* Limited by the LLM context window for very large webpages.

---

# 📚 Learning Outcomes

After completing this project, you will understand:

* AI Agent Architecture
* Tool Calling
* LangChain Tools
* Agent Loops
* Groq API Integration
* Web Search Integration
* Web Scraping
* Prompt Engineering
* Markdown Report Generation
* Modular AI Application Design
* Production-Ready Project Organization

---

# 🤝 Contributing

Contributions are welcome!

Possible improvements:

* Better planning strategies
* Additional search providers
* Improved prompts
* Better error handling
* More export formats
* Memory support
* Multi-agent workflows

---

# ⭐ Acknowledgements

* Groq for ultra-fast LLM inference
* Meta for the Llama models
* LangChain for agent abstractions
* DuckDuckGo for web search
* BeautifulSoup for HTML parsing

---

# 👨‍💻 Author

Built as a hands-on learning project while exploring **Generative AI**, **AI Agents**, **Tool Calling**, **Prompt Engineering**, **LLM Applications**, and **Production-Ready AI Systems**.
