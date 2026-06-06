# 🌍 CityMind AI

> An Agentic AI-powered City Intelligence Assistant that delivers real-time weather updates, latest city news, and AI-generated insights through an interactive modern interface.

---

## 🚀 About The Project

CityMind AI is a smart city assistant built using **CrewAI**, **OpenAI GPT-4o-mini**, **Tavily Search**, and **OpenWeather API**.

Instead of using a traditional chatbot workflow, CityMind AI follows an **Agentic AI architecture**, where an intelligent AI agent decides which tools to use, gathers live information, and generates a structured city report.

Users can simply enter a city name and receive:

* 🌤 Current weather conditions
* 📰 Latest city-related news
* 🤖 AI-generated city insights
* 📊 Structured and readable reports

---

## ✨ Features

### 🌤 Real-Time Weather Intelligence

* Current temperature
* Feels-like temperature
* Humidity
* Weather condition
* Wind speed

### 📰 Live News Retrieval

* Latest city news
* News summaries
* Source links

### 🤖 Agentic AI Workflow

* Tool calling with CrewAI
* Autonomous decision making
* Multi-source information gathering

### 🎨 Modern User Interface

* Glassmorphism design
* Dark theme
* Animated components
* Responsive layout
* Premium user experience

---

## 🧠 Architecture

```text
                ┌─────────────┐
                │    User     │
                └──────┬──────┘
                       │
                       ▼
              ┌────────────────┐
              │  CrewAI Agent  │
              └──────┬─────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
 ┌───────────────┐      ┌────────────────┐
 │ Weather Tool  │      │   News Tool    │
 │ OpenWeather   │      │     Tavily     │
 └───────┬───────┘      └────────┬───────┘
         │                       │
         └──────────┬────────────┘
                    ▼
          ┌───────────────────┐
          │ GPT-4o-mini LLM   │
          └─────────┬─────────┘
                    ▼
          ┌───────────────────┐
          │ Structured Report │
          └───────────────────┘
```

---

## 🛠 Technology Stack

### Frontend

* Streamlit
* HTML/CSS
* Custom Glassmorphism UI

### AI Framework

* CrewAI
* OpenAI GPT-4o-mini

### APIs

* OpenWeather API
* Tavily Search API

### Programming Language

* Python

---

## 📂 Project Structure

```text
CityMind-AI/
│
├── app.py
├── crew_agents.py
├── Tools.py
├── requirements.txt
├── README.md
├── .env
│
└── assets/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/CityMind-AI.git
```

### Navigate To Project

```bash
cd CityMind-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key

OPENWEATHER_API_KEY=your_openweather_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 💡 Example Queries

```text
Mumbai

Delhi

Pune

Nagpur

Bangalore
```

The AI agent will automatically gather weather data and the latest news for the selected city.

---

## 🔄 Agent Workflow

1. User enters a city name
2. CrewAI agent receives the request
3. Agent invokes the weather tool
4. Agent invokes the news tool
5. Live information is collected
6. GPT-4o-mini generates a structured report
7. Results are displayed in the UI

---

## 📈 Future Enhancements

* Multi-Agent Collaboration
* Voice Assistant Support
* Interactive Maps Integration
* Travel Recommendations
* Historical Weather Analytics
* Cloud Deployment
* User Authentication
* Real-Time Alerts
* Mobile-Friendly Version

---

## 🧑‍💻 Author

**Himanshu Namdeo**

Automation Engineer | Python Developer | AWS Certified | AI Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub and sharing it with others.

---

### Built with ❤️ using CrewAI, OpenAI, Tavily, Streamlit, and OpenWeather.
