# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
import os

config = aai.TranscriptionConfig(language_code="pt")

aai.settings.api_key = "0e31eb2cf6e54b708adbcefde65848dc"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe(os.getcwd() + os.sep +'data' + os.sep + 'video'  + os.sep + 'teste.mp4')
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)