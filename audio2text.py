import io
import os
from tqdm import tqdm
from google.cloud import speech_v1p1beta1 as speech

def transcrever_audio(nome_arquivo, pbar):
    client = speech.SpeechClient()

    # Carrega o arquivo de áudio
    with io.open(nome_arquivo, "rb") as audio_file:
        conteudo = audio_file.read()

    audio = speech.RecognitionAudio(content=conteudo)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        language_code="pt-BR",
    )

    # Envia a requisição de transcrição de fala
    response = client.recognize(config=config, audio=audio)

    # Processa a resposta para extrair o texto reconhecido
    texto_transcrito = ""
    for result in response.results:
        texto_transcrito += result.alternatives[0].transcript + " "

    return texto_transcrito.strip()

# Substitua 'audio.mp3' pelo caminho onde você quer salvar o arquivo de áudio
audio_path = os.getcwd() + os.sep +'data' + os.sep + 'audio'  + os.sep + 'teste.wav'

# Cria barra de progresso
with tqdm(total=100, desc='Transcrevendo áudio') as pbar:
    texto_transcrito = transcrever_audio(audio_path, pbar)

print("\nTexto transcrito:")
print(texto_transcrito)
