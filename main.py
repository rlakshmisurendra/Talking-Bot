import os
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# Configure the Generative AI API
genai.configure(api_key="AIzaSyCjhXKKta38Uk1GqdINRa90boQ62Odt-fI")

# Create the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

chat_session = model.start_chat(history=[])

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

try:
    with sr.Microphone() as source:
        print("Please say something... (listening)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

    # Compose the query
    instruction = "Instruction: talk like a expert in the feild of question "
    question = instruction + text
    response = chat_session.send_message(question)

    # Output the response
    print(response.text)
    engine.say(response.text)
    engine.runAndWait()

except sr.WaitTimeoutError:
    print("Listening timed out while waiting for a phrase to start.")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from the speech recognition API; {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
