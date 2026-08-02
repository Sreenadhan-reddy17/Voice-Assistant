import streamlit as st
import speech_recognition as sr
import datetime
import os
from dotenv import load_dotenv
import requests
import json
from gtts import gTTS
import base64
from io import BytesIO

load_dotenv()
recognizer = sr.Recognizer()
try:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found.")
except Exception as e:
    st.error(f"API key error: {str(e)}")
    st.stop()
# Text-to-Speech
def text_to_speech(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        st.error(f"TTS error: {e}")
        return None

def get_quote():
    try:
        response = requests.get("https://dummyjson.com/quotes/random", timeout=4)
        if response.status_code == 200:
            data = response.json()
            return f"“{data['quote']}” — {data['author']}"
    except Exception:
        pass
    return "“The secret of getting ahead is getting started.” — Mark Twain"



def autoplay_audio(audio_bytes):
    audio_base64 = base64.b64encode(audio_bytes.read()).decode('utf-8')
    audio_tag = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """
    st.html(audio_tag)

# AI API Call
def get_ai_response(prompt):
    # Use OpenRouter models with :free tag to support 0-credit accounts
    models_to_try = [
        "google/gemma-4-26b-a4b-it:free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "deepseek/deepseek-r1:free",
        "meta-llama/llama-3.1-8b-instruct:free",
        "mistralai/mistral-7b-instruct:free",
        "qwen/qwen-2.5-72b-instruct:free",
        "openrouter/auto"
    ]
    for model in models_to_try:
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a helpful voice assistant. Keep responses short and natural."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 150
            }
            response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                     headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"].strip()
            elif response.status_code in (402, 404):
                # 402 = Insufficient credits (paid model on free key)
                # 404 = Model endpoint unavailable
                continue
            else:
                st.error(f"OpenRouter API error: {response.text}")
                return "Something went wrong."
        except Exception as e:
            st.error(f"API call error: {e}")
            return "Error occurred."
    return "Could not reach an AI model endpoint. Please check your OpenRouter key."
# Basic Commands
def handle_basic_commands(command):
    command = command.lower()
    now = datetime.datetime.now()
    if "time" in command:
        return f"The current time is {now.strftime('%I:%M %p')}."
    elif "date" in command:
        return f"Today's date is {now.strftime('%B %d, %Y')}."
    elif "day today" in command:
        return f"Today is {now.strftime('%A')}."
    return None
# Theme Setup (Dark & Light)
def apply_theme(theme="dark"):
    if theme == "dark":
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

            html, body, .stApp {
                background: linear-gradient(135deg, #090D16 0%, #0F172A 50%, #1E1B4B 100%);
                color: #F8FAFC !important;
                font-family: 'Outfit', -apple-system, sans-serif;
            }

            /* Titles */
            h1, h2, h3 {
                background: linear-gradient(90deg, #FFFFFF 0%, #38BDF8 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 700 !important;
                letter-spacing: -0.5px;
            }

            h4, h5, h6 {
                color: #38BDF8 !important;
                font-weight: 600 !important;
            }

            /* Crisp body and markdown text */
            p, span, label, li, div {
                color: #F8FAFC;
            }

            .stMarkdown p, .stMarkdown div {
                color: #F8FAFC !important;
                -webkit-text-fill-color: initial !important;
            }

            /* Input Box */
            .stTextInput > div > div > input {
                background-color: #1E293B !important;
                color: #FFFFFF !important;
                border: 2px solid #38BDF8 !important;
                border-radius: 12px !important;
                padding: 12px 16px !important;
                font-size: 15px !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
            }

            .stTextInput > div > div > input::placeholder {
                color: #94A3B8 !important;
            }

            .stTextInput > div > div > input:focus {
                border-color: #818CF8 !important;
                box-shadow: 0 0 15px rgba(56, 189, 248, 0.4) !important;
            }

            /* Send Button */
            .stFormSubmitButton > button {
                background: linear-gradient(135deg, #FF8C00 0%, #FFD700 100%) !important;
                color: #000000 !important;
                border: none !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                font-size: 15px !important;
                box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4) !important;
                transition: all 0.25s ease-in-out !important;
                width: 100% !important;
            }

            .stFormSubmitButton > button:hover {
                transform: translateY(-2px) scale(1.02) !important;
                box-shadow: 0 6px 20px rgba(255, 215, 0, 0.6) !important;
            }

            /* Single Half Moon Round Button at top right */
            .st-key-theme_toggle > button {
                border-radius: 50% !important;
                width: 46px !important;
                height: 46px !important;
                min-width: 46px !important;
                padding: 0 !important;
                font-size: 22px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                margin-left: auto !important;
                background: #1E293B !important;
                border: 2px solid #FFD700 !important;
                box-shadow: 0 0 15px rgba(255, 215, 0, 0.5) !important;
                transition: transform 0.2s ease !important;
            }

            .st-key-theme_toggle > button:hover {
                transform: rotate(20deg) scale(1.1) !important;
            }

            /* Read Button Styling */
            div[class*="st-key-read_"] > button {
                width: auto !important;
                padding: 0.35em 1em !important;
                font-size: 13px !important;
                font-weight: 600 !important;
                border-radius: 8px !important;
                margin-left: auto !important;
                background: linear-gradient(135deg, #0284C7 0%, #38BDF8 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                box-shadow: 0 2px 8px rgba(56, 189, 248, 0.3) !important;
            }

            div[class*="st-key-read_"] > button:hover {
                transform: translateY(-1px) !important;
                box-shadow: 0 4px 12px rgba(56, 189, 248, 0.5) !important;
            }

            /* Divider */
            hr {
                border: none !important;
                border-top: 1px solid #334155 !important;
                margin: 1.5em 0 !important;
            }

            /* Alert / Quote Cards */
            .stAlert {
                border-left: 5px solid #FFD700 !important;
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border-radius: 10px !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
            }

            /* Audio Player */
            .stAudio {
                filter: invert(0.9) hue-rotate(180deg) brightness(1.2);
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

            html, body, .stApp {
                background: linear-gradient(135deg, #F0F4F8 0%, #E2E8F0 50%, #DBEAFE 100%);
                color: #0F172A !important;
                font-family: 'Outfit', -apple-system, sans-serif;
            }

            /* Titles */
            h1, h2, h3 {
                background: linear-gradient(90deg, #0F172A 0%, #0284C7 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 700 !important;
                letter-spacing: -0.5px;
            }

            h4, h5, h6 {
                color: #0284C7 !important;
                font-weight: 600 !important;
            }

            /* Crisp body and markdown text */
            p, span, label, li, div {
                color: #0F172A;
            }

            .stMarkdown p, .stMarkdown div {
                color: #0F172A !important;
                -webkit-text-fill-color: initial !important;
            }

            /* Input Box */
            .stTextInput > div > div > input {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 2px solid #0284C7 !important;
                border-radius: 12px !important;
                padding: 12px 16px !important;
                font-size: 15px !important;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
            }

            .stTextInput > div > div > input::placeholder {
                color: #64748B !important;
            }

            .stTextInput > div > div > input:focus {
                border-color: #2563EB !important;
                box-shadow: 0 0 15px rgba(2, 132, 199, 0.3) !important;
            }

            /* Send Button */
            .stFormSubmitButton > button {
                background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                font-size: 15px !important;
                box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35) !important;
                transition: all 0.25s ease-in-out !important;
                width: 100% !important;
            }

            .stFormSubmitButton > button:hover {
                transform: translateY(-2px) scale(1.02) !important;
                box-shadow: 0 6px 18px rgba(2, 132, 199, 0.5) !important;
            }

            /* Single Half Moon Round Button at top right */
            .st-key-theme_toggle > button {
                border-radius: 50% !important;
                width: 46px !important;
                height: 46px !important;
                min-width: 46px !important;
                padding: 0 !important;
                font-size: 22px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                margin-left: auto !important;
                background: #FFFFFF !important;
                border: 2px solid #0284C7 !important;
                box-shadow: 0 2px 10px rgba(2, 132, 199, 0.3) !important;
                transition: transform 0.2s ease !important;
            }

            .st-key-theme_toggle > button:hover {
                transform: rotate(20deg) scale(1.1) !important;
            }

            /* Read Button Styling */
            div[class*="st-key-read_"] > button {
                width: auto !important;
                padding: 0.35em 1em !important;
                font-size: 13px !important;
                font-weight: 600 !important;
                border-radius: 8px !important;
                margin-left: auto !important;
                background: linear-gradient(135deg, #0F172A 0%, #334155 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                box-shadow: 0 2px 8px rgba(15, 23, 42, 0.25) !important;
            }

            div[class*="st-key-read_"] > button:hover {
                transform: translateY(-1px) !important;
                box-shadow: 0 4px 12px rgba(15, 23, 42, 0.4) !important;
            }

            /* Divider */
            hr {
                border: none !important;
                border-top: 1px solid #CBD5E1 !important;
                margin: 1.5em 0 !important;
            }

            /* Alert / Quote Cards */
            .stAlert {
                border-left: 5px solid #0284C7 !important;
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border-radius: 10px !important;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05) !important;
            }

            /* Audio Player */
            .stAudio {
                filter: brightness(1.0);
            }
            </style>
        """, unsafe_allow_html=True)

# Main App
def main():
    st.set_page_config(page_title="AI Voice Assistant", layout="centered", page_icon="🧠")
    
    # Initialize session state (theme, turns, quote)
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'
    if 'turns' not in st.session_state:
        st.session_state.turns = []
    if 'playing_idx' not in st.session_state:
        st.session_state.playing_idx = None
    if 'daily_quote' not in st.session_state:
        st.session_state.daily_quote = get_quote()

    apply_theme(st.session_state.theme)

    # Top Header with Title and Half-Moon Round Theme Toggle Button (Top Right Corner)
    top_col1, top_col2 = st.columns([6, 1])
    with top_col1:
        st.markdown("## 🤖 AI Voice Assistant")
        st.markdown("<small style='color:gray;'>Your personal voice-based AI.</small>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🌙", key="theme_toggle", help="Toggle Light / Dark Theme"):
            st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
            st.rerun()

    st.markdown("---")

    st.markdown("### 💡 Quote of the Day")
    st.success(st.session_state.daily_quote)

    # --- Input Section (Top) ---
    st.subheader("💬 Ask Something")

    with st.form(key="chat_form", clear_on_submit=True, border=False):
        col_input, col_btn = st.columns([5, 1])
        with col_input:
            user_input = st.text_input("Your message...", placeholder="e.g., What's the time?", label_visibility="collapsed")
        with col_btn:
            submitted = st.form_submit_button("🎤 Send")

    if submitted and user_input.strip():
        basic_response = handle_basic_commands(user_input)
        if basic_response:
            response = basic_response
        else:
            with st.spinner("Thinking..."):
                response = get_ai_response(user_input)

        # Save turn without auto-playing voice
        st.session_state.turns.append({
            "user": user_input,
            "assistant": response,
            "audio": None
        })
        st.session_state.playing_idx = None
        st.rerun()

    # Helper colors for theme-aware message cards
    is_dark = st.session_state.theme == "dark"

    user_bg = "rgba(30, 41, 59, 0.85)" if is_dark else "#E0F2FE"
    user_border = "#FFD700" if is_dark else "#0284C7"
    user_label_color = "#FFD700" if is_dark else "#0369A1"
    user_text_color = "#F8FAFC" if is_dark else "#0F172A"

    asst_bg = "rgba(15, 23, 42, 0.9)" if is_dark else "#FFFFFF"
    asst_border = "#334155" if is_dark else "#CBD5E1"
    asst_label_color = "#38BDF8" if is_dark else "#0284C7"
    asst_text_color = "#F8FAFC" if is_dark else "#0F172A"
    asst_shadow = "0 4px 15px rgba(0,0,0,0.3)" if is_dark else "0 2px 10px rgba(0,0,0,0.05)"

    # --- Active Response (Directly below the chat box) ---
    if st.session_state.turns:
        active_idx = len(st.session_state.turns) - 1
        current_turn = st.session_state.turns[active_idx]
        st.markdown("---")

        st.markdown(f"""
            <div style="background-color: {user_bg}; padding: 12px 16px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid {user_border};">
                <strong style="color: {user_label_color};">You:</strong> <span style="color: {user_text_color};">{current_turn['user']}</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div style="background-color: {asst_bg}; padding: 14px 18px; border-radius: 10px; margin-bottom: 6px; border: 1px solid {asst_border}; box-shadow: {asst_shadow};">
                <strong style="color: {asst_label_color};">Assistant:</strong> <span style="color: {asst_text_color};">{current_turn['assistant']}</span>
            </div>
        """, unsafe_allow_html=True)

        # Read Button aligned to bottom right corner
        r_col1, r_col2 = st.columns([5, 1])
        with r_col2:
            if st.button("🔊 Read", key=f"read_act_{active_idx}", help="Listen to this response"):
                st.session_state.playing_idx = active_idx

        # Play voice if Read button was clicked for this active turn
        if st.session_state.playing_idx == active_idx:
            if not current_turn.get("audio"):
                with st.spinner("Generating audio..."):
                    current_turn["audio"] = text_to_speech(current_turn["assistant"])
            if current_turn.get("audio"):
                autoplay_audio(current_turn["audio"])
                st.audio(current_turn["audio"], format='audio/mp3')

    # --- Conversation History (Previous messages below active response) ---
    if len(st.session_state.turns) > 1:
        st.markdown("---")
        st.subheader("📜 Conversation History")
        # Display past turns in reverse order (newer history on top, older below)
        for idx in range(len(st.session_state.turns) - 2, -1, -1):
            turn = st.session_state.turns[idx]

            st.markdown(f"""
                <div style="background-color: {user_bg}; padding: 12px 16px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid {user_border};">
                    <strong style="color: {user_label_color};">You:</strong> <span style="color: {user_text_color};">{turn['user']}</span>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="background-color: {asst_bg}; padding: 14px 18px; border-radius: 10px; margin-bottom: 6px; border: 1px solid {asst_border}; box-shadow: {asst_shadow};">
                    <strong style="color: {asst_label_color};">Assistant:</strong> <span style="color: {asst_text_color};">{turn['assistant']}</span>
                </div>
            """, unsafe_allow_html=True)

            # Read Button aligned to bottom right corner
            h_col1, h_col2 = st.columns([5, 1])
            with h_col2:
                if st.button("🔊 Read", key=f"read_hist_{idx}", help="Listen to this response"):
                    st.session_state.playing_idx = idx

            # Play voice if Read button was clicked for this history turn
            if st.session_state.playing_idx == idx:
                if not turn.get("audio"):
                    with st.spinner("Generating audio..."):
                        turn["audio"] = text_to_speech(turn["assistant"])
                if turn.get("audio"):
                    autoplay_audio(turn["audio"])
                    st.audio(turn["audio"], format='audio/mp3')

            st.markdown(f"<hr style='border-top: 1px solid {'#334155' if is_dark else '#CBD5E1'};'>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()