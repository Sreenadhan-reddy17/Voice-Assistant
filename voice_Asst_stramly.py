import streamlit as st
import speech_recognition as sr
import pyttsx3
import datetime # For current time/date responses

st.set_page_config(page_title="Rule-Based Voice Assistant Bot", layout="centered")


# Use st.cache_resource to initialize the pyttsx3 engine only once
@st.cache_resource
def get_pyttsx3_engine():
    """Initializes and returns the pyttsx3 engine, caching it."""
    engine = pyttsx3.init()
    return engine

# Initialize the text-to-speech engine once using the cached function
engine = get_pyttsx3_engine()

def speak(text):
    """Converts text to speech."""
    try:
        # Stop any currently running speech to avoid conflicts (optional, but good practice)
        engine.stop() 
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"Text-to-speech error: {e}")

def recognize_speech():
    """Listens for speech and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        r.adjust_for_ambient_noise(source) # Adjust for ambient noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10) # Add timeout for better UX
            st.success("Processing audio...")
            command = r.recognize_google(audio, language='en-IN') # Specify Indian English
            st.write(f"You said: \"{command}\"")
            return command.lower() # Convert to lowercase for easier rule matching
        except sr.UnknownValueError:
            st.warning("Sorry, I did not understand that. Please try again.")
            return None
        except sr.WaitTimeoutError:
            st.warning("No speech detected within the timeout period. Please try again.")
            return None
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}\n"
                     "Please check your internet connection. Speech recognition requires an internet connection.")
            return None
        except Exception as e:
            st.error(f"An unexpected error occurred during speech recognition: {e}")
            return None

def get_rule_based_response(command):
    """Generates a response based on predefined rules/keywords."""
    if not command:
        return "I didn't hear anything. Can you please repeat?"

    command = command.lower() # Ensure command is lowercase for matching

    if "hello" in command or "hi" in command:
        return "Hello there! How can I help you today?"
    elif "how are you" in command:
        return "I'm just a computer program, so I don't have feelings, but I'm ready to assist you!"
    elif "your name" in command:
        return "I am a voice assistant created in Streamlit."
    elif "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p") # e.g., 10:05 AM
        return f"The current time is {current_time}."
    elif "date" in command:
        now = datetime.datetime.now()
        current_date = now.strftime("%B %d, %Y") # e.g., June 10, 2025
        return f"Today's date is {current_date}."
    elif "your location" in command or "where are you" in command:
        # Based on your previous context
        return "I exist in the digital realm, but my current physical location is in Hyderabad, Telangana, India, where my code is running."
    elif "thank you" in command or "thanks" in command:
        return "You're welcome! Is there anything else?"
    elif "goodbye" in command or "bye" in command:
        return "Goodbye! Have a great day."
    elif "open google" in command:
        st.write("Opening Google...")
        # Note: Streamlit runs on the server, so os.system('start chrome google.com')
        # will open Chrome on the server, not the user's browser.
        # This is more for demonstration of an action.
        return "I can't open applications directly on your browser through Streamlit, but you can navigate there manually."
    else:
        return "I'm sorry, I don't have a specific response for that. Can you ask something else?"

def main():
    st.title("🗣️ General-Purpose Voice Assistant AI Bot (Rule-Based)")
    st.markdown("---")

    # Use a session state variable to manage listening status
    # The 'listening' state manages whether the recognition process should start
    if 'listening_active' not in st.session_state:
        st.session_state.listening_active = False
    if 'last_command' not in st.session_state:
        st.session_state.last_command = None


    col1, col2 = st.columns([1, 2])

    with col1:
        # This button triggers the listening process
        if st.button("🎙️ Start Listening", use_container_width=True):
            st.session_state.listening_active = True
            st.session_state.last_command = None # Reset command on new listen
            st.rerun() # Force rerun to start listening immediately


    # Only run speech recognition if 'listening_active' is True
    if st.session_state.listening_active:
        command = recognize_speech()
        # After recognition attempt, set listening_active to False
        st.session_state.listening_active = False # Stop listening after one attempt

        if command:
            st.session_state.last_command = command # Store the command for display
            # Force rerun to display the response and prevent re-listening immediately
            st.rerun() 
        else:
            # If no command was recognized or an error occurred, just rerun
            st.rerun()

    # Display results and speak only if a command was successfully received
    if st.session_state.last_command:
        with st.spinner("Generating response..."):
            response_text = get_rule_based_response(st.session_state.last_command)
        
        st.markdown("---")
        st.subheader("Bot's Response:")
        st.info(response_text)
        
        # Speak the response
        speak(response_text)
        
        # Clear the last command so the bot doesn't speak it again on next rerun
        st.session_state.last_command = None


    with col2:
        st.subheader("Instructions:")
        st.write("""
        1. Click the "🎙️ Start Listening" button.
        2. Speak clearly when "Listening..." appears.
        3. The bot will respond based on predefined rules.
        4. Ensure your microphone is connected and allowed by your browser.
        """)
        st.markdown("---")
        st.subheader("Capabilities (Rule-Based):")
        st.write("""
        * Basic greetings ("Hello", "Hi")
        * Self-introduction ("What is your name?")
        * Current time and date ("What time is it?", "What's the date today?")
        * Location ("Where are you?", "Your location")
        * Acknowledgements ("Thank you")
        * Farewells ("Goodbye")
        * Generic fallback for unknown commands.
        """)
        st.write("Developed by an expert Streamlit developer (that's me! 😉)")


if __name__ == "__main__":
    main()