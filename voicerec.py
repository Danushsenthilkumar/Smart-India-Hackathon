import os
import torchaudio
import speech_recognition as sr
from transformers import pipeline
from textblob import TextBlob



# Create the sentiment analysis pipeline without specifying a model
nlp_pipeline = pipeline("sentiment-analysis")

# Specify the path to the WAV audio file you want to analyze
audio_file_path = "depressed.dat.wav"

# Check if the audio file exists
if not os.path.exists(audio_file_path):
    print(f"Audio file not found at '{audio_file_path}'")
else:
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Load and transcribe the WAV audio file using Google Web Speech API
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
            transcribed_text = recognizer.recognize_google(audio_data)

        # Perform sentiment analysis on the transcribed text
        sentiment_result = nlp_pipeline(transcribed_text)

        # Perform audio-based sentiment analysis (you may need to replace this with a specialized audio sentiment analysis model)
        audio_sentiment_score = 0.5  # Placeholder for audio sentiment score

        # Calculate the combined sentiment score out of 10
        combined_sentiment_score = (sentiment_result[0]['score'] + audio_sentiment_score) * 5

        # Ensure the score is within the range [0, 10]
        combined_sentiment_score = min(10, max(0, combined_sentiment_score))

        print(f"Transcribed Text: {transcribed_text}")
        print(f"Combined Sentiment Score (out of 10): {combined_sentiment_score:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
