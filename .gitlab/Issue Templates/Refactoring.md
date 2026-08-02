## 🧹 Code Refactoring – Modularize App Logic for Maintainability

### Target Area

The `app.py` file currently handles all input/output logic, voice recording, audio playback, and API interaction in one file. This leads to poor readability and difficulty in scaling the codebase for new features like image input or context memory.

### Problem Description

Having everything in a single file makes it hard to:
- Test components in isolation
- Debug issues in specific logic (e.g., API timeout vs. gTTS failure)
- Add new modules (e.g., chat export, OCR input)

### Refactoring Goals

- Extract Claude-3 interaction into `api_handler.py`
- Move audio playback logic to `audio_engine.py`
- Create `voice_input.py` for speech recognition
- Keep `app.py` limited to UI and Streamlit state management

### Suggested Approach

Split logic into a `src/` directory:
