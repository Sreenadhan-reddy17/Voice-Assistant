# 🤖 AI Voice Assistant

A web-based AI voice assistant built with Python and Streamlit. It answers questions using OpenRouter AI models, provides built-in quick commands (time, date, day), and converts responses into spoken audio on demand.

---

## ✨ Features

- **AI Powered Chat**: Integrated with OpenRouter API (supports free AI models like Gemma, Llama, and DeepSeek).
- **Text-to-Speech (TTS)**: Dedicated **🔊 Read** button on assistant responses for spoken voice playback.
- **Quick Local Commands**: Answers current time, date, and day of the week instantly.
- **Quote of the Day**: Displays an inspiring daily quote on app launch.
- **Dark & Light Themes**: Easily switch between dark and light modes using theme toggle button.
- **Organized Chat History**: Displays your active prompt and response right below the input box, archiving older messages below.

---

## 🛠 Tech Stack

- **Frontend / Web UI**: Streamlit
- **AI Models**: OpenRouter API (`requests`)
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Environment**: Python, `python-dotenv`

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Key
Create a `.env` file in the root project directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 3. Run the Application
```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.
