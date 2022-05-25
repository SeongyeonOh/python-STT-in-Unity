import os
# Imports the Google Cloud client library
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\SOGANG\Documents\development\unity\STT\Assets\speech-to-text.json"
# Instantiates a client
client = speech.SpeechClient()

# file_name = input("Enter a file name(with the extension name) : ")
# The name of the audio file to transcribe
# gcs_uri = f"gs://speech_to_txt_bucket/{file_name}"
gcs_uri = f"gs://speech_to_txt_bucket/sample_mono.wav"

audio = speech.RecognitionAudio(uri=gcs_uri)

# Google의 기본 인코딩 타입
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=44100,
#     language_code="en-US",
# )

# 변경된 인코딩 타입
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
    sample_rate_hertz=44100,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))