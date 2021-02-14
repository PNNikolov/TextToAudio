from gtts import gTTS
import os

fh = open("text.txt", "r")
my_text = fh.read().replace("\n", " ")

# my_text = "Text to speech Auto Reader program"

language = 'en'

output = gTTS(text=my_text, lang=language, slow=False)

output.save("text to audio.mp3")
fh.close()
os.system("start text audio.mp3")
