from moviepy.editor import VideoFileClip


def extrair_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

# Substitua 'video.mp4' pelo caminho do seu arquivo de vídeo
video_path = '/workspaces/video_transcribe/data/video/10000000_280508027886481_2376169689188899108_n.mp4'

# Substitua 'audio.mp3' pelo caminho onde você quer salvar o arquivo de áudio
audio_path = '/workspaces/video_transcribe/data/audio/10000000_280508027886481_2376169689188899108_n.mp3'

extrair_audio(video_path, audio_path)
