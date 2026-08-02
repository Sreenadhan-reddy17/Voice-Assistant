## 🐞 Bug Fix Merge Request

### ✅ Summary of the Bug
Clearly describe the issue this MR resolves:
- Voice not recognized under noisy conditions.
- gTTS response not playing after response.

### 🛠️ What was fixed?
- Improved speech recognition fallback.
- Ensured proper playback by handling temp audio file lifecycle.

### 🧪 How to Test?
1. Use the voice input in both quiet and noisy environments.
2. Ask a query like "What is the time?"
3. Check if audio playback happens properly.

### 📷 Screenshots / Logs (if any)
_Include before/after logs or errors if relevant._

### 📎 Related Issues
Closes #<issue_number>
