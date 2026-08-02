## 📚 Documentation Update – Missing Voice Input Setup Instructions

### Section Needing Update

The README currently covers Streamlit installation, OpenRouter API usage, and TTS playback using gTTS. However, it does not clearly guide users on setting up their microphone or configuring the `speech_recognition` package for real-time voice input, which is essential for this project.

### Current Content

There is a mention of “Click mic to speak,” but no installation or configuration guide for dependencies like `PyAudio`, which is crucial for microphone usage.

### Updated/Corrected Content

Add the following section under "Installation":

```markdown
### 🔊 Enabling Voice Input

To enable real-time speech input, install PyAudio:

#### On Windows:
