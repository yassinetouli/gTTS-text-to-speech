# gTTS-text-to-speech

A simple Python project that converts text into an MP3 audio file using **gTTS (Google Text-to-Speech)**.

## 📌 Description

This project demonstrates how to use the `gTTS` Python library to convert written text into spoken audio.

The application takes the following text:

```text
Hello, My name is Yassine.
```

and generates an audio file named:

```text
output.mp3
```

## 🛠️ Technologies Used

* **Python 3.11**
* **gTTS (Google Text-to-Speech)**

## 📦 Installation

Make sure Python is installed:

```bash
python --version
```

Then install `gTTS`:

```bash
python -m pip install gTTS
```

If you are using the Python installation from `C:\Python311`:

```powershell
C:\Python311\python.exe -m pip install gTTS
```

## 🚀 Usage

Create a Python file, for example:

```text
text_to_speech.py
```

Add the following code:

```python
from gtts import gTTS

text = "Hello, My name is Yassine."

tts = gTTS(text=text, lang='en')

tts.save("output.mp3")

print("Audio file 'output.mp3' has been created successfully.")
```

Run the program:

```bash
python text_to_speech.py
```

After successful execution, you should see:

```text
Audio file 'output.mp3' has been created successfully.
```

The generated `output.mp3` file will be located in the same directory as the Python script.

## 🌍 Changing the Language

The `lang` parameter determines the language used for speech synthesis.

For example:

```python
tts = gTTS(text="Bonjour, je m'appelle Yassine.", lang="fr")
```

Some common language codes:

| Language | Code |
| -------- | ---- |
| English  | `en` |
| French   | `fr` |
| Spanish  | `es` |
| German   | `de` |
| Italian  | `it` |
| Arabic   | `ar` |

## 📁 Project Structure

```text
Text_speech/
│
├── text_to_speech.py
└── output.mp3
```

`output.mp3` is generated automatically when the Python script is executed.

## ⚠️ Requirements

gTTS requires an **Internet connection** because it communicates with Google's text-to-speech service.
