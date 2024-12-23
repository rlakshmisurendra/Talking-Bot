# Talking Bot

Talking Bot is a Python-based application that combines speech recognition, text-to-speech, and Google Generative AI to create an interactive voice assistant. Users can ask questions via voice, and the bot responds with expert-level insights using AI.

---

## Features
- **Speech Recognition**: Captures user input through a microphone.
- **Generative AI**: Uses Google Generative AI (Gemini) to generate intelligent responses.
- **Text-to-Speech**: Converts AI responses into spoken words.
- **Customizable Prompts**: Tailors the bot's response style (e.g., expert-level answers).

---

## Prerequisites

1. **Python 3.7 or later**
   Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/)

2. **Dependencies**
   Install the required Python libraries:
   ```bash
   pip install SpeechRecognition pyttsx3 google-generativeai
   ```

3. **Google Generative AI API Key**
   - Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Generative AI API.

4. **Microphone**
   A functional microphone is required for capturing audio input.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/talking-bot.git
   cd talking-bot
   ```

2. Add your API key to the script:
   Replace `your-api-key` in the script:
   ```python
   genai.configure(api_key="your-api-key")
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

1. **Start the Bot**:
   Run `main.py` to start the application.

2. **Speak to the Bot**:
   - Wait for the prompt: `Please say something... (listening)`.
   - Ask a question aloud (e.g., "What is the purpose of life?").

3. **Get a Response**:
   - The bot will analyze your query and provide an AI-generated response.
   - Listen to the spoken response or view it in the console.

---

## Customization

### Modify AI Response Style
Change the instruction variable to customize the response style:
```python
instruction = "Instruction: talk like a field expert "
```

### Adjust AI Configuration
Modify `generation_config` to control AI behavior:
```python
"temperature": 0.7,  # Creativity level
"top_p": 0.9,        # Sampling strategy
"max_output_tokens": 512  # Maximum response length
```

---

## Troubleshooting

1. **PyAudio Installation Error**:
   - For Windows, download the appropriate `.whl` file from [Unofficial Python Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install:
     ```bash
     pip install path/to/pyaudio.whl
     ```

2. **API Key Error**:
   - Ensure the API key is correct and active.
   - Check for typos in the `genai.configure` line.

3. **Speech Recognition Issues**:
   - Ensure your microphone is working.
   - Adjust ambient noise levels using:
     ```python
     recognizer.adjust_for_ambient_noise(source)
     ```

---



## Contributing

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request with a detailed description of your changes.

---

