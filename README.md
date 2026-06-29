# Autonomous Market Intelligence Platform

An enterprise-style **Multi-Agent AI Market Intelligence Platform** built using **LangGraph**, **FastAPI**, **Streamlit**, **Gemini 2.5 Flash**, and **Tavily Search**.

The platform autonomously performs market research, competitor analysis, trend discovery, business strategy generation, campaign content creation, PDF/JSON report generation, and exposes the complete workflow through both a **Streamlit UI** and **FastAPI REST API**.

---

# What's New (Latest Version)

Compared to the previous version, this project now includes:

* FastAPI REST API integration
* Docker support
* JSON report export
* Agent execution time tracking
* Token usage tracking
* AI cost estimation
* Improved competitor analysis
* Improved trend summaries
* Official competitor websites
* Research timestamps
* Better PDF reporting
* Dynamic LangGraph thread IDs
* Production-ready project structure

---

# Features

### AI Multi-Agent Workflow

* Market Research Agent
* Competitor Analysis Agent
* Industry Trend Agent
* Strategy Generation Agent
* Human Approval Layer
* Campaign Content Agent

### Reporting

* Professional PDF Market Report
* Campaign PDF Report
* JSON Export
* Research Sources
* Research Timestamps

### AI Monitoring

* Execution Time per Agent
* Token Usage per Agent
* Estimated Gemini Cost
* Workflow Metrics

### Backend

* FastAPI REST API
* Streamlit Frontend
* Docker Ready
* Memory Persistence using LangGraph MemorySaver

---

# API Documentation

After running FastAPI:

http://127.0.0.1:8000/docs

Swagger automatically provides interactive API testing.

Endpoints

POST /generate

Generate complete market intelligence report.

POST /generate-content

Generate campaign content from approved strategy.

---

# Workflow

User

↓

Streamlit UI / FastAPI

↓

LangGraph StateGraph

↓

Market Agent

↓

Competitor Agent + Trend Agent (Parallel)

↓

Strategy Agent

↓

Human Approval

↓

Content Agent

↓

PDF + JSON Export

---

# Technology Architecture

User

↓

Streamlit UI

↓

FastAPI

↓

LangGraph

├── StateGraph

├── MemorySaver

├── Router

└── Multi-Agent System

↓

Gemini 2.5 Flash

↓

Pydantic Structured Outputs

↓

Tavily Search API

---

# Folder Structure

```text
autonomous-market-intelligence

│

├── app

│ ├── agents

│ ├── api

│ ├── graph

│ ├── prompts

│ ├── schemas

│ ├── tools

│ ├── utils

│ ├── report_pdf_generator.py

│ ├── campaign_pdf_generator.py

│ ├── json_export.py

│ ├── llm.py

│ └── memory.py

│

├── ui.py

├── main.py

├── Dockerfile

├── requirements.txt

└── README.md
```

---

# Tech Stack

### AI

* LangGraph
* LangChain
* Gemini 2.5 Flash
* Tavily Search

### Backend

* FastAPI
* Pydantic

### Frontend

* Streamlit

### Reporting

* ReportLab
* JSON Export

### Deployment

* Docker

---

# Installation

```bash
git clone <repository-url>

cd autonomous-market-intelligence

pip install -r requirements.txt
```

---

# Environment Variables

Create a .env file

```text
GOOGLE_API_KEY=YOUR_API_KEY

TAVILY_API_KEY=YOUR_API_KEY
```

---

# Run Streamlit

```bash
streamlit run ui.py
```

---

# Run FastAPI

```bash
uvicorn app.api.api:app --reload
```

---

# Docker

Build

```bash
docker build -t market-intelligence .
```

Run

```bash
docker run -p 8501:8501 market-intelligence
```

---

# Output

The platform generates

* Market Intelligence Report
* Competitor Analysis
* Industry Trend Analysis
* Business Strategy
* LinkedIn Post
* Marketing Email
* Google Ad Copy
* Professional PDF Reports
* JSON Report
* API Response

---

# Future Improvements

* Authentication
* Database Integration
* Dashboard Analytics
* Multi-user Sessions
* Cloud Deployment
* CI/CD Pipeline
* Live Monitoring
* Kubernetes Deployment
