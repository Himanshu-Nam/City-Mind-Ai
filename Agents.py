
# =========================================================
# 🌍 CityMind AI
# Smart AI Powered City Assistant
# =========================================================

# -------------------------
# Load Environment Variables
# -------------------------
from dotenv import load_dotenv
load_dotenv()

# -------------------------
# Import Libraries
# -------------------------
import os
import time
import requests
import streamlit as st

from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

# =========================================================
# WEATHER TOOL
# =========================================================
@tool
def get_weather(city: str) -> str:
    """
    Get current weather of a city
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city},IN&appid={api_key}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if str(data.get("cod")) != "200":
        return f"❌ Unable to fetch weather for {city}"

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    return f"""
## 🌤 Weather in {city}

- 🌡 Temperature: {temp}°C
- 🤗 Feels Like: {feels_like}°C
- 💧 Humidity: {humidity}%
- ☁ Condition: {desc}
"""


# =========================================================
# NEWS TOOL
# =========================================================
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def get_news(city: str) -> str:
    """
    Get latest news about a city
    """

    response = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=3
    )

    results = response.get("results", [])

    if not results:
        return f"❌ No news found for {city}"

    news = f"## 📰 Latest News in {city}\n\n"

    for i, r in enumerate(results, start=1):

        title = r.get("title", "No title")
        url = r.get("url", "")
        snippet = r.get("content", "")

        news += f"""
### {i}. {title}

🔗 {url}

📝 {snippet[:120]}...

"""

    return news


# =========================================================
# OPENAI MODEL
# =========================================================
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# =========================================================
# CREATE AGENT
# =========================================================
agent = create_agent(
    model=model,
    tools=[get_weather, get_news],

    system_prompt="""
You are CityMind AI.

You are a smart city assistant.

You help users with:
- Weather updates
- City news
- Smart responses

Keep responses short and clean.
"""
)


# =========================================================
# STREAMLIT CONFIG
# =========================================================
st.set_page_config(
    page_title="CityMind AI",
    page_icon="🌍",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

/* Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(
        -45deg,
        #0f172a,
        #111827,
        #1e293b,
        #0f172a
    );

    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: white;
}

/* Background Animation */
@keyframes gradientBG {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

/* Main Title */
.main-title {

    text-align: center;
    font-size: 60px;
    font-weight: 700;
    color: #38bdf8;

    animation: glow 2s infinite alternate;
}

/* Glow Animation */
@keyframes glow {

    from {
        text-shadow: 0 0 10px #38bdf8;
    }

    to {
        text-shadow: 0 0 30px #38bdf8;
    }
}

/* Subtitle */
.subtitle {

    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* User Bubble */
.user-bubble {

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );

    padding: 15px;
    border-radius: 18px;
    margin-bottom: 15px;
    margin-left: 25%;

    color: white;

    box-shadow: 0 5px 15px rgba(37,99,235,0.4);

    animation: slideRight 0.4s ease;
}

/* Bot Bubble */
.bot-bubble {

    background: linear-gradient(
        135deg,
        #059669,
        #10b981
    );

    padding: 15px;
    border-radius: 18px;
    margin-bottom: 15px;
    margin-right: 25%;

    color: white;

    box-shadow: 0 5px 15px rgba(5,150,105,0.4);

    animation: slideLeft 0.4s ease;
}

/* User Animation */
@keyframes slideRight {

    from {
        opacity: 0;
        transform: translateX(30px);
    }

    to {
        opacity: 1;
        transform: translateX(0px);
    }
}

/* Bot Animation */
@keyframes slideLeft {

    from {
        opacity: 0;
        transform: translateX(-30px);
    }

    to {
        opacity: 1;
        transform: translateX(0px);
    }
}

/* Sidebar */
section[data-testid="stSidebar"] {

    background: rgba(15,23,42,0.95);
    border-right: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================
st.markdown("""
<div class="main-title">
🌍 CityMind AI
</div>

<div class="subtitle">
Your Smart AI Powered City Assistant 🚀
</div>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# CHAT DISPLAY
# =========================================================
for role, message in st.session_state.messages:

    if role == "user":

        st.markdown(
            f"""
            <div class="user-bubble">
            👤 <b>You</b><br><br>
            {message}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="bot-bubble">
            🤖 <b>CityMind AI</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(message)


# =========================================================
# USER INPUT
# =========================================================
user_input = st.chat_input(
    "Ask weather, news, or city updates..."
)


# =========================================================
# HANDLE CHAT
# =========================================================
if user_input:

    # Save User Message
    st.session_state.messages.append(
        ("user", user_input)
    )

    # Display User Message
    st.markdown(
        f"""
        <div class="user-bubble">
        👤 <b>You</b><br><br>
        {user_input}
        </div>
        """,
        unsafe_allow_html=True
    )

    # AI Thinking
    with st.spinner("🤖 CityMind AI is thinking..."):

        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        })

        bot_reply = result["messages"][-1].content

    # Bot Bubble
    st.markdown(
        """
        <div class="bot-bubble">
        🤖 <b>CityMind AI</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # TYPEWRITER EFFECT
    # =====================================================
    placeholder = st.empty()

    full_text = ""

    for char in bot_reply:

        full_text += char

        placeholder.markdown(full_text)

        time.sleep(0.005)

    # Save Bot Message
    st.session_state.messages.append(
        ("bot", bot_reply)
    )


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("## 🌍 CityMind AI")

    st.write("""
### ⚡ Features

✅ Live Weather Updates

✅ Latest City News

✅ AI Powered Responses

✅ Animated Modern UI

✅ Smart City Assistant
""")

    st.divider()

    st.markdown("### 🛠 Tech Stack")

    st.write("""
- Streamlit
- LangChain
- OpenAI
- Tavily API
- OpenWeather API
""")

    st.divider()

    st.success("🚀 CityMind AI Ready")

