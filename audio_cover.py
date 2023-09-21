from gtts import gTTS

language=input("ENTER THE LANGUAGE CODE:")

# Text to be converted to speech
text ="This is a sample text to be converted to speech."

# Initialize the gTTS object
tts = gTTS(text, lang=language)

# Specify the filename for the WAV audio file
audio_file_name = "output2.wav"

# Save the audio as a WAV file
tts.save(audio_file_name)

print(f"Audio file '{audio_file_name}' saved successfully in WAV format.")






