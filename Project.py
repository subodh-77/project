import speech_recognition as sr
import os
from AppOpener import open
import webbrowser
import pyttsx3
import streamlit as st

# Initialize the speech engine (for local use, not directly in Streamlit UI loop)
engine = pyttsx3.init()
engine.setProperty('rate', 140)

# Define the speak function but modify it for compatibility
def speak(text):
    # To avoid the RuntimeError, avoid running this in Streamlit's main UI loop.
    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass

def speech_reco():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        st.write("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        st.write("Error with the speech recognition service.")
        return ""

def shutdown():
    os.system("shutdown /s /t 1")

def open_paint():
    open("Paint")

def open_chrome():
    open("Microsoft Edge")

def open_vscode():
    open("Visual Studio Code")

def open_notepad():
    open("Notepad")

def open_youtube():
    webbrowser.open('https://www.youtube.com/?gl=IN')

def open_instagram():
    webbrowser.open('https://www.instagram.com/?hl=en')

# Streamlit UI
st.title("Voice Assistant GUI")
st.write("Hi! How can I assist you today?")

# Optionally, add a text command interpreter
def handle_command(command):
    if "open chrome" in command:
        st.write("Opening Chrome...")
        open_chrome()
    elif "open vs code" in command:
        st.write("Opening Visual Studio Code...")
        open_vscode()
    elif "open paint" in command:
        st.write("Opening Paint...")
        open_paint()
    elif "shut down" in command:
        st.write("Shutting down the PC in 3 seconds...")
        shutdown()
    elif "youtube" in command:
        st.write("Opening YouTube...")
        open_youtube()
    elif "instagram" in command:
        st.write("Opening Instagram...")
        open_instagram()
    elif "notepad" in command:
        st.write("Opening Notepad...")
        open_notepad()
    elif "stop" in command:
        st.write("Going to sleep...")
        st.stop()

# Add buttons for actions
if st.button("Speak Command"):
    command = speech_reco()
    st.write(f"Command recognized: {command}")
    handle_command(command)

# Add manual buttons for each action (for convenience)
if st.button("Open Chrome"):
    open_chrome()
if st.button("Open VS Code"):
    open_vscode()
if st.button("Open Paint"):
    open_paint()
if st.button("Shutdown PC"):
    shutdown()
if st.button("Open YouTube"):
    open_youtube()
if st.button("Open Instagram"):
    open_instagram()
if st.button("Open Notepad"):
    open_notepad()
