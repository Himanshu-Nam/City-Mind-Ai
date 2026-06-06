
from dotenv import load_dotenv
load_dotenv()

import time
import streamlit as st
from crew_agents import crew

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="CityMind AI",
    page_icon="🌍",
    layout="wide",
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #334155 100%
    );
}

/* Hide Streamlit Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hero Section */
.hero {
    text-align: center;
    padding: 40px 20px;
}

.hero-title {
    font-size: 72px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #c084fc
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #cbd5e1;
    font-size: 22px;
    margin-top: 10px;
}

/* Search Container */
.search-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 24px;
    padding: 25px;
    margin-top: 20px;
    margin-bottom: 20px;
    animation: floatCard 4s ease-in-out infinite;
}

@keyframes floatCard {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-5px);}
    100% {transform: translateY(0px);}
}


            /* Search Input */
.stTextInput input {

    background: rgba(255,255,255,0.08) !important;

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);

    color: #ffffff !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    border-radius: 18px !important;

    height: 70px !important;

    font-size: 17px !important;

    padding-left: 18px !important;

    transition: all 0.3s ease !important;

    box-shadow:
        0 4px 20px rgba(0,0,0,0.15),
        inset 0 1px 0 rgba(255,255,255,0.05);
}

/* Focus Effect */
.stTextInput input:focus {

    border: 1px solid rgba(96,165,250,0.7) !important;

    box-shadow:
        0 0 0 3px rgba(59,130,246,0.15),
        0 8px 30px rgba(59,130,246,0.25) !important;
}

/* Placeholder */
.stTextInput input::placeholder {

    color: rgba(255,255,255,0.55) !important;

    font-weight: 400;
}

/* Button */
.stButton button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;
    color: white;
    font-weight: 700;
    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );
    transition: all .3s ease;
}

.stButton button:hover {
    transform: translateY(-3px);
}


/* Result Card */
.result-card {

    background: rgba(15, 23, 42, 0.75);

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 35px;

    margin-top: 25px;

    color: #f8fafc;

    line-height: 1.8;

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.05);

    animation: fadeIn .5s ease;

    transition: all .3s ease;
}

.result-card:hover {

    transform: translateY(-4px);

    box-shadow:
        0 15px 45px rgba(0,0,0,0.45),
        0 0 25px rgba(99,102,241,0.15);
}

/* Markdown headings */
.result-card h1,
.result-card h2,
.result-card h3 {
    color: #60a5fa;
    margin-top: 10px;
}

/* Bold text */
.result-card strong {
    color: #c084fc;
}

/* Lists */
.result-card ul li {
    margin-bottom: 8px;
}

/* Links */
.result-card a {
    color: #38bdf8;
    text-decoration: none;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
    <div class="hero">
    <div class="hero-title">
          CityMind AI 🌍
    </div>
    <div class="hero-subtitle">
        Weather • News • AI Insights
    </div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# SEARCH BOX
# --------------------------------------------------

#st.markdown('<div class="search-card">', unsafe_allow_html=True)

col1, col2 = st.columns([7,2])

with col1:
    city = st.text_input(
        "",
        placeholder="🔍 Type any city..."
    )

with col2:
    st.write("")
    search = st.button(
        "🚀 Explore",
        use_container_width=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# SEARCH ACTION
# --------------------------------------------------

if search and city:

    status = st.empty()

    loading_steps = [
        "🌍 Collecting city information...",
        "🌤 Fetching weather data...",
        "📰 Reading latest news...",
        "🤖 Generating AI summary..."
    ]

    for step in loading_steps:
        status.info(step)
        time.sleep(0.6)

    try:

        result = crew.kickoff(
            inputs={
                "city": city
            }
        )

        status.empty()

        answer = (
            result.raw
            if hasattr(result, "raw")
            else str(result)
        )

        
      #  st.markdown("""
        #<div class="result-card">
        #""", unsafe_allow_html=True)

        st.markdown(answer)

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ {e}")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
Built with ❤️ using CrewAI • Tavily • OpenWeather • OpenAI
</div>
""", unsafe_allow_html=True)

