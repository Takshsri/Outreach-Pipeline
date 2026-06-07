# AI Outreach Pipeline

## Overview

AI Outreach Pipeline is a Python-based backend automation system that streamlines lead generation and outreach workflows using real-world API integrations.

The pipeline automatically:

* Finds similar companies using Ocean.io
* Enriches company intelligence using Prospeo
* Discovers verified business contacts and work emails
* Prepares outreach-ready lead data
* Sends automated outreach emails using Brevo

This project demonstrates backend engineering concepts including API orchestration, modular service architecture, environment-based configuration management, workflow automation, lead enrichment pipelines, and real-world third-party API integration.

---

# Features

* Similar company discovery using Ocean.io
* Company enrichment using Prospeo
* Verified business contact discovery
* Work email extraction
* Automated outreach email sending using Brevo
* Lead preparation workflow layer inspired by EazyReach
* Secure API key management with `.env`
* Modular Python service architecture
* REST API integration
* JSON response parsing
* Error handling for failed requests
* Automated workflow chaining without manual intervention

---

# Technologies Used

* Python
* Requests
* dotenv
* Ocean.io API
* Prospeo API
* Brevo API

---

# Project Structure

```bash
outreach-pipeline/
│
├── main.py
├── config.py
├── requirements.txt
├── .env
│
├── services/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── brevo.py
│   └── eazyreach.py
│
└── README.md
```

---

# Workflow Architecture

```text
Input Company Domain
        ↓
Ocean.io Similar Company Discovery
        ↓
Prospeo Company Enrichment
        ↓
Prospeo Contact Discovery
        ↓
Verified Work Email Extraction
        ↓
Lead Preparation Layer
        ↓
Brevo Outreach Automation
```

---

# API Integrations

## Ocean.io

Ocean.io is used for lookalike company discovery.

Example:

```bash
amazon.com
    ↓
walmart.com
snapdeal.com
marksandspencer.com
```

The API helps identify businesses with similar characteristics for outreach targeting.

---

## Prospeo

Prospeo is used for:

* Company enrichment
* Business intelligence
* Contact discovery
* LinkedIn profile retrieval
* Verified work email extraction

### Extracted Data

* Company Name
* Industry
* Employee Count
* Location
* LinkedIn Profile
* Contact Name
* Job Title
* Verified Work Email

### Important API Update

During development, older Prospeo endpoints such as:

```bash
/linkedin-email-finder
```

were deprecated by Prospeo.

The project was migrated to the newer Prospeo APIs using:

```bash
/search-person
```

This updated workflow now directly retrieves verified business contacts and work emails from the search response.

---

## Brevo

Brevo is used for automated outreach email delivery.

The pipeline automatically sends outreach emails to verified business contacts discovered during the enrichment stage.

---

## EazyReach Layer

The EazyReach module acts as a lead-preparation layer inside the workflow.

It structures enriched lead information into outreach-ready data before email automation.

---

# Installation Setup

## 1. Clone Repository

```bash
git clone https://github.com/Takshsri/Outreach-Pipeline
```

---

## 2. Navigate to Project

```bash
cd outreach-pipeline
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
OCEAN_API_KEY=your_ocean_api_key
PROSPEO_API_KEY=your_prospeo_api_key
BREVO_API_KEY=your_brevo_api_key
```

---

# Running the Project

Run the application:

```bash
python main.py
```

---

# Example Workflow

## Input

```bash
Enter company domain: amazon.com
```

---

## Output

```bash
Similar Companies:

1. walmart.com
2. snapdeal.com
3. marksandspencer.com

Company Details:

Company Name : Walmart
Industry     : General Retail
Employees    : 556121
Location     : United States
LinkedIn     : https://www.linkedin.com/company/walmart

Verified Contact:

Name      : Chavis Mahoney
Title     : Manager II, Operations InHome Delivery Launch Team
LinkedIn  : https://www.linkedin.com/in/chavis-mahoney-a170a526a
Email     : c*******@walmart.com

Outreach email sent successfully
```

---

# Engineering Concepts Demonstrated

* REST API Integration
* Backend Workflow Automation
* Environment Variable Management
* JSON Response Parsing
* API Error Handling
* Modular Service Architecture
* Third-Party API Orchestration
* Lead Enrichment Pipelines
* Outreach Automation
* Business Contact Discovery
* Email Automation Systems

---

# Future Improvements

* CSV lead export
* Database integration
* Async workflow execution
* Campaign analytics dashboard
* Frontend admin dashboard
* Scheduled outreach automation
* AI-generated personalized email copy
* Multi-contact enrichment
* Retry and queue systems

---

# Author

Maya Mannam

Backend Developer | Python Developer | API Integration Enthusiast
