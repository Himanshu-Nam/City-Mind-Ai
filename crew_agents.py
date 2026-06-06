from crewai import Agent, Task, Crew, Process

from crewai import LLM
from Tools import get_weather, get_news

llm = LLM(
    model="gpt-4o-mini"
   
)

city_agent = Agent(
    role="Smart City Assistant",
    goal="Provide weather and latest city news",
    backstory="""
    You are an intelligent city assistant.

    Your job:
    - Fetch weather information
    - Fetch latest city news
    - Create a clean summary
    """,
    tools=[get_weather, get_news],
    llm=llm,
    verbose=True
)

city_task = Task(
    description="""
    The user wants information about the city: {city}

    Your responsibilities:

    1. Use the get_weather tool to fetch current weather.
    2. Use the get_news tool to fetch the latest news.
    3. Analyze both results.
    4. Create a professional city report.

    The report should contain:

    ## 🌤 Current Weather
    - Temperature
    - Feels Like
    - Humidity
    - Weather Condition

    ## 📰 Latest News
    - Top 5 headlines
    - Short summary of each headline

    ## 🤖 AI Summary
    - Overall city situation
    - Important events
    - Weather insights

    Make the output user-friendly and well formatted in Markdown.
    """,
    expected_output="""
    A structured markdown report containing:
    - Current weather details
    - Latest city news
    - AI generated summary
    """,
    agent=city_agent
)
crew = Crew(
    agents=[city_agent],
    tasks=[city_task],
    process=Process.sequential,
    verbose=False
)