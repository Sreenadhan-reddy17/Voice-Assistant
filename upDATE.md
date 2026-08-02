# 🗣 AI Voice Assistant

A lightweight, browser-based voice assistant built with **Python**, **Streamlit**, and **Claude-3** via **OpenRouter API**. It supports both voice and text input, and responds using AI-generated speech powered by `gTTS`.

---

## 📌 Overview

**AI Voice Assistant** enables users to interact with AI using voice or text in a clean, user-friendly browser interface. It combines speech recognition, natural language understanding, and text-to-speech capabilities to create an accessible and intelligent conversational assistant.

---

## 🎯 Key Features

- 🎤 Text and voice input  
- 🤖 AI-powered responses via Claude-3  
- 🔊 Audio playback using `gTTS`  
- 📆 Answers basic commands like date, time, and day  
- 🧾 Complete conversation history display  
- 🌐 Hosted on Hugging Face Spaces for public use  

---

## ⚙️ How It Works

1. Accepts input through text box or microphone  
2. Converts speech to text using `speech_recognition`  
3. Simple queries (e.g., "What's the time?") are handled locally  
4. Complex queries are sent to Claude-3 via OpenRouter API  
5. Response is displayed and converted to speech using `gTTS`  
6. Audio is played directly in the browser using `streamlit_audio`  

---

## 🚀 Use Cases

- 💬 Personal AI assistant for daily productivity  
- ♿ Voice-based interface for visually or physically impaired users  
- 🎓 Educational tool for practicing speech interaction  
- 🧪 Prototype for hands-free AI and multimodal interfaces  

---

## 🧩 Extension: Multimodal Smart Assistant

The assistant can be extended to support **image, location, and context-based interactions**, making it more intelligent and versatile.

### 🔥 Advanced Features

- 📸 **Image Input Support**  
  Upload or capture images for AI analysis (object detection, OCR, image captioning)

- 🧠 **Contextual Memory**  
  Maintains history of previous interactions for coherent conversations

- 🎙️ **Wake Word Detection**  
  Continuous listening mode with hotword triggers (e.g., "Hey Ava")

- 📍 **Location-Based Responses**  
  Personalized responses using user’s location (e.g., weather updates)

- 🧑‍💻 **Task Execution Mode**  
  Perform system-level tasks like opening apps, setting reminders, etc.

- 📄 **Export Chat Logs**  
  Download full chat history in `.txt` or `.pdf` format  

---

## 🛠 Tech Stack

| Feature              | Libraries/Tools                          |
|----------------------|------------------------------------------|
| AI Response          | Claude-3 via OpenRouter API              |
| Voice Input          | `speech_recognition`, Snowboy            |
| Text-to-Speech       | `gTTS`                                   |
| Image Handling       | OpenCV, Pillow, CLIP                     |
| UI                   | Streamlit, `streamlit_chat`, `streamlit_audio` |
| Voice Activation     | Porcupine, Snowboy                       |
| Location Awareness   | `geocoder`                               |
| Task Execution       | `pyautogui`, `PyWhatKit`                 |
| PDF Export           | `fpdf`, `reportlab`                      |

---

## 🧪 Advanced Use Case Scenarios

- ♿ Enhanced accessibility for users with motor or visual impairments  
- 🎓 Interactive learning assistant with visual input and feedback  
- 🧠 Smart document reader for OCR, form filling, and summaries  
- 🏡 Integration-ready with smart homes, IoT systems, and virtual bots  

---

## 💡 Future Improvements

- Integrate multilingual TTS  
- Add voice emotion recognition  
- Build mobile-first UI with offline support  
- Integrate real-time AI vision with camera feed  
- Enable API token management through UI  

---

## 📂 Repository Structure (Example)

