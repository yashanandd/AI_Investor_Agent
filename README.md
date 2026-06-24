# AI Investment Research Agent

## Overview

AI Investment Research Agent is an AI-powered investment analysis platform that researches a company, evaluates its financial health, analyzes recent news, identifies risks, and generates an investment recommendation with a confidence score.

The application uses a LangGraph workflow to orchestrate multiple AI-powered analysis stages and present the results through an interactive dashboard.

---

## Features

* Company Research & Business Analysis
* Financial Metrics Evaluation
* Recent News Analysis
* Risk Assessment
* Investment Recommendation
* Confidence Score Generation
* Interactive Dashboard
* LangGraph Workflow Orchestration
* Groq LLM Integration

---

## Architecture

```text
Frontend (Next.js)

        ↓

FastAPI Backend

        ↓

LangGraph Workflow

    ├── Company Research Node
    ├── Financial Analysis Node
    ├── News Analysis Node
    ├── Risk Analysis Node
    └── Decision Node

        ↓

Groq LLM

        ↓

Investment Recommendation
```

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* LangGraph
* LangChain
* Groq

### Data Sources

* Yahoo Finance
* Yahoo Query
* News Scraping

---

## Installation

### Backend

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

## Environment Variables

### Backend (.env)

```env
GROQ_API_KEY=your_groq_api_key
```

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## Example Workflow

### Input

```text
Tesla
```

### Processing Pipeline

1. Company Research
2. Financial Analysis
3. News Analysis
4. Risk Assessment
5. Investment Recommendation

### Output

* Company Analysis
* Financial Analysis
* News Summary
* Risk Assessment
* Recommendation
* Confidence Score

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Analysis Result

![Analysis Result](screenshots/analysis-result.png)

### Recommendation Dashboard

![Recommendation](screenshots/recommendation.png)

---

## Live Deployment

### Frontend

Frontend Link Here

### Backend

Backend Link Here

---

## Future Improvements

* Real-Time Market Data Integration
* Historical Stock Charts
* Portfolio Recommendation Engine
* Multi-Agent Research Workflow
* Company Comparison Feature
* PDF Report Generation
* Watchlist Management
* User Authentication

---

## Author

**Yash Anand**

B.Tech Computer Science & Engineering
Lovely Professional University

InsideIIM × Altuni AI Labs – AI Product Development Engineer Assignment
