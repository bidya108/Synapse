# Synapse 🧠

### AI & ML Weekly News Digest

Synapse is an automated AI & ML news digest that collects recent developments, generates concise AI-powered summaries, and compiles them into a clean, shareable PDF report.

## ✨ Features

- 📰 Curates AI & ML news
- 🤖 AI-powered article summarization using Gemini
- 📄 Automatically generates PDF reports
- 📅 Date-based news organization
- ⚡ Demo Mode for instant testing without API calls
- 🔐 Secure API key management with environment variables

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Guardian News API
- Pandas
- ReportLab
- uv

## 🚀 Getting Started

### 1. Install dependencies

```bash
uv sync
2. Configure API Keys

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key
GUARDIAN_API_KEY=your_guardian_api_key
3. Run Synapse

For live AI & ML news:

uv run python main.py

For instant testing with built-in demo news:

uv run python main.py --demo
📂 Project Structure
synapse/
├── components/
│   ├── get_news.py
│   └── generate_pdf.py
├── pipelines/
│   └── supervisor.py
├── prompts/
│   └── summary_prompt.txt
└── utils/
    ├── llm_utils.py
    ├── logger.py
    └── config.py

main.py
pyproject.toml
uv.lock
📄 Output

Generated reports are organized by date inside the data/ directory.

🔒 Security

API credentials are stored in .env and excluded from version control. Never commit API keys or other sensitive credentials to GitHub.
