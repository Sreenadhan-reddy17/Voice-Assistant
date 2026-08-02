# 📄 Project Report: Voice Assistant using AI & Streamlit

# REPORT.md

## 1. Team Information

*Team Name:* Tech Innovators

*Team Members:*

| Name             | Role                |
| ---------------- | ------------------- |
| Upendar          | Project Lead        |
| Pranav           | AI Engineer         |
| Sreenadhan Reddy | Frontend Developer  |
| Suchitra         | UX Designer         |
| Sai Reddy        | Quality Assurance   |

**Individual Contributions:**

* *Upendar: Coordinated team efforts, managed project timeline, and ensured deliverables were met*

* *Pranav: Integrated speech recognition using speech\_recognition library and implemented OpenRouter API connection*

* *Sreenadhan Reddy: Built the Streamlit interface with conversation history and multimodal interaction*

* *Suchitra: Designed the voice/text input flow and response presentation*

* *Sai Reddy: Conducted user testing and gathered feedback from external users*

---
## 2. Application Overview

*Application Name:* AI Voice Assistant

*Use Case & Problem Solved:*
Many users, especially the elderly or those with limited tech skills, struggle to interact with digital systems through traditional UI. Our voice-based AI assistant solves this by enabling natural, hands-free conversations.

*Target Users:*
General users, particularly those who prefer or need voice-based interaction — e.g., elderly, visually impaired, or multitaskers.

*Key Features:*

* Voice and text input modes
* AI-powered conversational responses
* Text-to-speech response playback
* Basic commands like time, date, and day
* Conversation history logging

*Motivation:*
We wanted to build a simple, intuitive assistant that leverages AI capabilities in real-time, focusing on accessibility and natural interaction.

---

## 3. AI Integration Details

*AI Model/Technique Used:*
* Model: claude-3 via OpenRouter
* Link: [OpenRouter](https://openrouter.ai)

*How AI Powers the Application:*

* Users type their queries.
* The input is either processed directly (for basic queries like "What is the time?") or sent to the claude-3 model via OpenRouter.
* The AI responds concisely and conversationally.
* The response is shown on the UI and converted to audio using gTTS.

*Prompt Engineering:*
We used a system-level prompt instructing the model to keep responses short and helpful. This improved interaction speed and relevance for a real-time assistant.

Prompt example:

json
{"role": "system", "content": "You are a helpful voice assistant. Keep responses concise and conversational (1-2 sentences max)."}


---

## 4. Technical Architecture & Development

*Overall Architecture Diagram:*
&#x20;

*Technology Stack:*

* Python
* Streamlit
* gTTS (Google Text-to-Speech)
* OpenRouter API (claude-3)
* SpeechRecognition
* Hugging Face Spaces (Deployment)

*Challenges & Solutions:*

1. *Speech Recognition Errors:* Initially faced issues with microphone access; resolved by handling missing dependencies and fallback UI.
2. *Streaming Audio:* Managing audio playback in browser required base64 encoding and custom HTML. Solved using autoplay <audio> tag.
3. *API Rate Limits:* Encountered request failures; added error handling and fallback messages.

*Open-Source Licensing:*

* *License:* MIT
* *Why:* Encourages open collaboration and reuse with minimal restrictions.

---

## 5. User Testing & Feedback

*Methodology:*
We shared the application with friends, family, and mentors — ensuring none were from our internship group. Feedback was collected via Google Forms.

*Summary of Feedback (10 Users):*

* *Usability:* 8/10 average
* *UI/UX:* 7.5/10 (dark mode)
* *AI Performance:* 9/10
* *Responsiveness:* 7/10 (noted minor lag in voice mode)
* *Value Proposition:* 8.5/10
* *Overall Satisfaction:* 8.5/10

*Most Common Praises:*

* Easy to use
* Natural voice responses
* Smooth integration of voice + AI

*Common Criticisms:*

* Delay in speech recognition
* No mobile view optimization

*Insights & Iterations:*

* Added audio feedback optimization
* Plan to enhance UI responsiveness

---

## 6. Future Roadmap & User Adoption Plan

*Future Roadmap:*

* *Phase 1 (Weeks 1–2):*

  * UI enhancements
  * Mobile layout optimization
  * Improve response delay in voice mode

* *Phase 2 (Weeks 3–4):*

  * Add support for multilingual input/output
  * Integrate weather and calendar APIs

* *Phase 3 (Weeks 5–6):*

  * Explore LLM fine-tuning for domain-specific skills (e.g., finance, travel)
  * Enable user profile memory across sessions

*User Adoption Plan:*

* *Target Audience Identification:*

  * Frequent users of productivity tools, tech enthusiasts, accessibility users
  * Platforms: Reddit r/Streamlit, Hugging Face Hub, Discord AI communities

* *Compelling Value Proposition:*

  * Hands-free AI interaction
  * Fast and friendly voice interface
  * Ideal for the elderly or multitaskers

* *Strategic Promotion:*

  * Share on Hugging Face Spaces and Streamlit forums
  * Create tutorials and demo videos
  * Submit to open-source showcases and GitHub trending projects

* *Frictionless Onboarding:*

  * In-app instructions on first launch
  * Simple UI with just two steps: input and hear response

* *Feedback & Iteration Loop:*

  * Add feedback form in UI
  * Encourage GitHub issues for suggestions/bugs

* *Open-Source Engagement:*

  * CONTRIBUTING.md with clear guidelines
  * Tags for good-first-issue in repository
  * Document structure for non-code contributions
---
## Submission Links
* *Code Repository:* https://code.swecha.org/ICFAI-tech-IP1/voiceassistant
* *Live App on Hugging Face:* https://huggingface.co/spaces/Sreenadhan-Reddy/VoiceAssistant-AI
* *Demo Video:* https://drive.google.com/file/d/1P7jUcdUq6owOGm4lXgDYIZhsAT7oY-_0/view?usp=sharing