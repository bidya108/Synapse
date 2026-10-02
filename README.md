# Synapse — AI-Powered Technology News Digest

Synapse is a Python-based automation project that collects technology and AI news from **The Guardian**, processes the article content using **Google Gemini**, and generates a formatted **PDF news digest** for a selected date.

The project combines web data extraction, AI-assisted content processing, and automated document generation into a single pipeline.

## How It Works

```text
The Guardian
     │
     ▼
Fetch Technology & AI Articles
     │
     ▼
Extract Article Content
     │
     ▼
Google Gemini
     │
     ▼
Generate News Summaries
     │
     ▼
Create PDF Digest
Features
Fetches technology and AI-related news from The Guardian
Supports date-based article collection
Extracts article titles, URLs, sections, publication dates, authors, and article content
Uses Google Gemini to transform extracted articles into concise news-style reports
Generates a structured PDF digest
Creates a cover page and individual article pages
Organizes generated reports by date
Includes logging for pipeline execution and errors
Uses a separate prompt file to control AI-generated content
Tech Stack
Programming
Python
Data Collection
The Guardian Content API
Requests
BeautifulSoup
AI
Google Gemini API
Document Generation
ReportLab
Data Processing
Pandas
Configuration
python-dotenv
Project Structure
synapse/
│
├── components/
│   ├── get_news.py
│   └── generate_pdf.py
│
├── config/
│   └── config.py
│
├── pipelines/
│   └── supervisor.py
│
├── prompts/
│   └── summary_prompt.txt
│
├── utils/
│   ├── llm_utils.py
│   └── logger.py
│
└── __init__.py
Pipeline
1. News Collection

Synapse uses The Guardian Content API to retrieve technology and AI-related articles for a selected date.

For each article, the system collects information such as:

Article title
Article URL
Section
Publication date
Author
Article content

The article page is then processed using BeautifulSoup to extract the available article text.

2. AI Content Processing

The extracted article content is sent to Google Gemini.

Synapse uses a separate prompt file to provide instructions for transforming the article into a concise, structured news report.

The generated content is then used as the main text for the PDF report.

3. PDF Generation

The processed articles are passed to the PDF generation component.

The generated report contains:

A cover page
The selected date
Individual article sections
Article titles
Generated article content

Reports are organized into date-based output folders.

4. Logging

The application includes logging to keep track of pipeline activity and errors during execution.

This makes it easier to monitor the different stages of the process and identify problems when they occur.

Output

Generated reports are organized by date.

Example:

data/
└── DD-MM-YYYY/
    └── Synapse DD-MM-YYYY.pdf

The final PDF acts as a compact technology and AI news digest for the selected date.

Configuration

Synapse requires API credentials for The Guardian and Google Gemini.

Create a .env file and provide the required credentials:

GUARDIAN_API_KEY=your_guardian_api_key
GEMINI_API_KEY=your_gemini_api_key

Keep your API keys private and do not commit the .env file to GitHub.

Running the Pipeline

The main pipeline accepts a date and processes the available articles for that date.

Example:

from synapse.pipelines.supervisor import run_pipeline

run_pipeline("2026-09-17")

The pipeline will:

Retrieve relevant articles from The Guardian
Extract the article content
Process the content using Google Gemini
Generate the PDF digest
Save the output in the corresponding date folder
Purpose

Synapse was built to explore how web data extraction, large language models, and automated document generation can be combined into a practical information-processing workflow.

The project focuses on turning raw online news content into a structured and readable PDF digest with minimal manual effort.
