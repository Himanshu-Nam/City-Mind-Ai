
import os
import requests

from crewai.tools import tool
from tavily import TavilyClient


# =====================================================
# WEATHER TOOL
# =====================================================

@tool("get_weather")
def get_weather(city: str) -> str:
    """
    Get current weather details for a city.
    """

    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
            return "OPENWEATHER_API_KEY not found in environment variables."

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if str(data.get("cod")) != "200":
            return f"Weather information not available for {city}"

        return f"""
City: {city}

Temperature: {data['main']['temp']}°C
Feels Like: {data['main']['feels_like']}°C
Humidity: {data['main']['humidity']}%
Condition: {data['weather'][0]['description']}
Wind Speed: {data['wind']['speed']} m/s
"""

    except Exception as e:
        return f"Weather API Error: {str(e)}"


# =====================================================
# NEWS TOOL
# =====================================================

@tool("get_news")
def get_news(city: str) -> str:
    """
    Fetch latest city news using Tavily.
    """

    try:

        tavily_api_key = os.getenv("TAVILY_API_KEY")

        if not tavily_api_key:
            return "TAVILY_API_KEY not found in environment variables."

        client = TavilyClient(api_key=tavily_api_key)

        response = client.search(
            query=f"latest news in {city}",
            search_depth="advanced",
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return f"No recent news found for {city}"

        news_items = []

        for idx, item in enumerate(results, start=1):

            title = item.get("title", "No Title")
            content = item.get("content", "")
            url = item.get("url", "")

            news_items.append(
                f"""
{idx}. {title}

Summary:
{content[:250]}

Source:
{url}
"""
            )

        return "\n".join(news_items)

    except Exception as e:
        return f"News API Error: {str(e)}"

