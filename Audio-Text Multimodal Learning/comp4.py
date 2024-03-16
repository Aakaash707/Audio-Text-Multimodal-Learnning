import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import speech_recognition as sr
from comp3 import *


def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Read the entire audio file
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")



def pull():

    # Specify the path to the folder containing audio files
    folder_path = "test_data"

    article_text = []

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".flac") or filename.endswith(".mp3") or filename.endswith(".wav"):
        # Access the audio file one by one
            audio_file_path = os.path.join(folder_path, filename)
            article_text.append(convert_audio_to_text(audio_file_path))

    article = ". ".join(article_text)

    return nltk_summarizer(article)

