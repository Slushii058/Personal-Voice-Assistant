import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        return command.lower()

def execute_command(command):
    """Execute commands based on the recognized text."""
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'wikipedia' in command:
        speak("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        try:
            result = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Can you be more specific? Here are some suggestions: {e.options}")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I could not find any information on that.")
    elif 'play music' in command:
        speak("Playing music")
        # Add the path to your local music directory or integrate with a music API
        webbrowser.open("https://www.spotify.com")  # Example: Opens Spotify
    else:
        speak("Sorry, I can only execute commands to open YouTube, search Wikipedia, or play music.")

def main():
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()
        if command:
            execute_command(command)
        if 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
