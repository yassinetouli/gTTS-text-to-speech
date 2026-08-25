from gtts import gTTS

text = "Hello, My name is Yassine."

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

print("Audio file 'output.mp3' has been created successfully.")