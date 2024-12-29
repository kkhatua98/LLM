from dotenv import load_dotenv 
load_dotenv()
import os 

from crewai_tools import SerperDevTool 

tool = SerperDevTool()