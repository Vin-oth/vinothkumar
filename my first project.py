import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):

    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "weather" in command:
        
        speak("The weather is sunny with a high of 75 degrees Fahrenheit.")
    elif "search" in command:
        
        speak("Here are the search results for your query.")
    else:
        speak("Sorry, I didn't understand that.")

def main():
    speak("Initializing voice assistant...")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            process_command(command)
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand audio.")
        except sr.RequestError:
            print("Could not request results. Please check your internet connection.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
