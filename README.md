Streamlit UI Input and Output screenshots:

<img width="1915" height="965" alt="image" src="https://github.com/user-attachments/assets/c98b42ce-94ee-4fb9-9144-fcca202a9618" />
<img width="1916" height="965" alt="image" src="https://github.com/user-attachments/assets/20b20a5c-ecc3-4ac3-9405-cbda4f7ccaaa" />
<img width="1917" height="962" alt="image" src="https://github.com/user-attachments/assets/52c83c86-aeba-498d-b095-167a02b956c7" />

I also attached the pdf report named market_report.pdf and campaign_content.pdf which we can be downloaded directly from the streamlit interface 

workFlow visualize:
                          USER
                            │
                            ▼
                    Streamlit UI
                            │
                            ▼
                   LangGraph Workflow
                            │
                            ▼
                    Market Agent
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
     Competitor Agent              Trend Agent
             │                             │
             └──────────────┬──────────────┘
                            ▼
                    Strategy Agent
                            │
                            ▼
                 Human Approval Layer
                            │
                 Yes ───────┴────── No
                  │                 │
                  ▼                 ▼
             Content Agent        End
                  │
                  ▼
       Campaign Content Generation
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Report PDF         Campaign PDF
        │                   │
        └─────────┬─────────┘
                  ▼
           Download via UI




Technology Architecture:

User
 │
 ▼
Streamlit UI
 │
 ▼
LangGraph
 │
 ├── StateGraph
 │
 ├── MemorySaver
 │
 ├── Router
 │
 └── Agents
        │
        ├── Market Agent
        ├── Competitor Agent
        ├── Trend Agent
        ├── Strategy Agent
        ├── Approval Agent
        └── Content Agent
                │
                ▼
            Gemini LLM
                │
                ▼
           Structured Output
          (Pydantic Schemas)
                │
                ▼
           Tavily Search API

          

Folder Architecture:

autonomous-market-intelligence
│
├── app
│   │
│   ├── agents
│   │   ├── market_agent.py
│   │   ├── competitor_agent.py
│   │   ├── trend_agent.py
│   │   ├── strategy_agent.py
│   │   ├── approval_agent.py
│   │   └── content_agent.py
│   │
│   ├── prompts
│   │   ├── market_prompt.py
│   │   ├── competitor_prompt.py
│   │   ├── strategy_prompt.py
│   │   └── content_prompt.py
│   │
│   ├── schemas
│   │   ├── market_schema.py
│   │   ├── competitor_schema.py
│   │   ├── strategy_schema.py
│   │   └── content_schema.py
│   │
│   ├── graph
│   │   ├── builder.py
│   │   ├── state.py
│   │   └── router.py
│   │
│   ├── tools
│   │   └── tavily_tool.py
│   │
│   ├── report_pdf_generator.py
│   ├── campaign_pdf_generator.py
│   ├── content_only.py
│   ├── memory.py
│   ├── llm.py
│   └── config.py
│
├── ui.py
├── requirements.txt
└── README.md



1. Project Title
   
# Autonomous Market Intelligence Platform

2. Project Description
## Overview

Autonomous Market Intelligence Platform is a LangGraph-based multi-agent AI system that performs market research, competitor analysis, trend discovery, strategic planning, content generation, and PDF reporting.

The system uses specialized AI agents working together to generate actionable business insights and marketing campaigns from a simple industry and business goal input.

3. Features
## Features

- Multi-Agent Architecture using LangGraph
- Market Research Agent
- Competitor Analysis Agent
- Industry Trend Analysis Agent
- Strategy Generation Agent
- Human-in-the-Loop Approval
- Marketing Content Generation
- PDF Report Export
- Campaign PDF Export
- Memory Persistence using MemorySaver
- Tavily Web Search Integration
- Streamlit User Interface

4. Tech Stack
## Tech Stack

- Python
- LangGraph
- LangChain
- Gemini
- Tavily Search
- Streamlit
- Pydantic
- ReportLab

5. Workflow
## Workflow

1. User enters Industry and Goal.
2. Market Agent performs market research.
3. Competitor Agent analyzes competitors.
4. Trend Agent identifies latest industry trends.
5. Strategy Agent generates business strategy.
6. User approves strategy.
7. Content Agent generates:
   - LinkedIn Post
   - Marketing Email
   - Google Ad Copy
8. PDF reports are generated.
9. User downloads reports.
    
6. Installation
## Installation

git clone <repository-url>

cd autonomous-market-intelligence

pip install -r requirements.txt

7. Environment Variables
## Environment Variables

Create a .env file and add:

GOOGLE_API_KEY=your_key
TAVILY_API_KEY=your_key

8. Run Application
## Run Application

streamlit run ui.py

