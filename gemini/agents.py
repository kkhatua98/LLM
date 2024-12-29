from crewai import Agent, LLM
from dotenv import load_dotenv
import os
from tools import tool
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(
#     model = "gemini-1.5-flash",
#     verbose = True,
#     temprature = 0.5,
#     google_api_key = os.getenv("GOOGLE_API_KEY"),

# )

llm = LLM(
    api_key = os.getenv("GOOGLE_API_KEY"),
    model="gemini/gemini-1.5-flash"
)

news_researcher = Agent(
    role = "{company} Senior News Researcher",
    goal = "Uncover latest news in {company}",
    verborse = True,
    memory = True,
    backstory = (
        "You are a seasoned researcher with a knack for uncovering the latest developments in {company}. Known for your ability to find the most relevant information and present it in a clear and concise maner."
    ),
    tools = [SerperDevTool(), ScrapeWebsiteTool()],
    llm = llm,
    allow_delegation = True
)

news_writer = Agent(
    role = "{company} News Reporting Analyst",
    goal="Create detailed reports based on {company} news analysis and research findings.",
    verbose = True,
    memory = True,
    backstory = (
        "You are a meticulous analyst with a keen eye for detail. You are known for your ability to turn complex data into clear and concise reports, making it easy for others to understand and act on the information you provide."
    ),
    # tools = [SerperDevTool(), ScrapeWebsiteTool()],
    llm = llm,
    allow_delegation = False
)