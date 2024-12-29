from crewai import Task
from tools import tool
from agents import news_researcher, news_writer
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

research_task = Task(
    description = (
        "Search news about {company}"
    ),
    expected_output="A list of news articles about {company} with the title, url and snippet",
    tools = [SerperDevTool(), ScrapeWebsiteTool()],
    agent=news_researcher
)

write_task = Task(
    description=(
        "Conduct a deep dive on the requested {company} and produce a detailed analysis of major factors influencing the stock price and growth. Conduct comprehensive research on the following topics and summarize the key points/findings under each category: Current pipeline and offerings, Supportive technology landscape, Adjacent technologies used to enhance and compliment its core portfolio, potential adjecent technologies that the {company} will invest/adopt in the future, Current competitors, Future competetion, Potential disruptive innovations and technologies, Other industry areas that would directly impact the companies' portfolio and growth, Dominance in sector, Expanision into New Markets, market expansion and global reach, strategic acquisitions and partnerships (list all), financial performance and growth, technological innvoations, technological advancements, adoption and product leadership, macro-economic factors (expand on each factor), forward looking strategies, regulatory environment, strategic vision and leadership, market performance (research market dynamics), market sentiment, investor sentiment and stock performance in the past quarter, breaking down key factors and their impact on stock price, news brief (include key news highlights and comprehensive list of YouTube videos)."
    ),
    expected_output="The output must contain detailed information and descriptions for each topic, specifically related to the {company}. It should use sub-bullets under each topic without restricting the number of sub-bullets, being thorough and extensive. Each sub-bullet should be expanded with a brief description. Include URLs to data sources, including {company} websites and a comprehensive list of recent YouTube video links. The GPT must avoid hallucinations and ensure all responses are grounded in the facts found via real time internet research, only providing information from verfiable sources. The responses must include as much information as possible for each topic and sub-bullet.",
    # tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)