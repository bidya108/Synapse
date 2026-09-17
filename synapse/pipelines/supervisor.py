import pandas as pd
from synapse.components.get_news import NewsScraper
from synapse.components.generate_pdf import GeneratePDF


def get_demo_news():
    return [
        {
            "title": "AI Agents Are Changing How Software Tasks Are Automated",
            "summary": "AI agents are increasingly being used to plan and complete multi-step software tasks. Modern systems combine language models with tools, memory and structured workflows to perform tasks with less manual intervention."
        },
        {
            "title": "Smaller AI Models Become More Practical for Everyday Applications",
            "summary": "Recent advances in model compression and efficient training are making smaller language models more useful. These models can reduce computing requirements while still providing strong performance for specific applications."
        },
        {
            "title": "Multimodal AI Brings Text, Image and Audio Together",
            "summary": "Multimodal artificial intelligence systems can process multiple types of information within a single workflow. This enables applications that combine text, images, audio and other forms of data."
        },
        {
            "title": "AI-Assisted Coding Continues to Expand",
            "summary": "AI coding tools are being used for code generation, debugging, documentation and software development assistance. Developers are increasingly combining these tools with traditional programming workflows."
        },
        {
            "title": "Research Focuses on More Efficient Machine Learning",
            "summary": "Machine learning research continues to explore ways of improving model efficiency, reducing computational costs and maintaining useful performance with fewer resources."
        }
    ]


def run_pipeline(date, demo=False):
    if demo:
        print("Running Synapse Daily in DEMO mode...")
        news = get_demo_news()
    else:
        print("Fetching live AI and ML news...")
        news_scraper = NewsScraper()
        news = news_scraper.extract(date)

    if not news:
        print("No news articles were collected.")
        return False

    news_df = pd.DataFrame(news)

    pdf = GeneratePDF(date)
    pdf.coverpage()

    for _, row in news_df.iterrows():
        pdf.innerpage(row["title"], row["summary"])

    pdf.save_pdf()

    print(f"PDF generated with {len(news_df)} articles.")
    return True