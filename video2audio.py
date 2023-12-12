from moviepy.editor import VideoFileClip
import os

def extrair_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

# Substitua 'video.mp4' pelo caminho do seu arquivo de vídeo
video_path = os.getcwd() + os.sep +'data' + os.sep + 'video'  + os.sep + 'teste.mp4'

# Substitua 'audio.mp3' pelo caminho onde você quer salvar o arquivo de áudio
audio_path = os.getcwd() + os.sep +'data' + os.sep + 'audio'  + os.sep + 'teste.wav'

extrair_audio(video_path, audio_path)
#print(os.getcwd())