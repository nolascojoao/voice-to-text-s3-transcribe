import speech_recognition as sr
import boto3
import time

s3_client = boto3.client('s3')
transcribe_client = boto3.client('transcribe')
bucket_name = "YOUR_BUCKET_NAME"  # Seu bucket S3
region = "us-east-1"  # Sua região

def record_audio(filename="audio.wav"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Gravando... Fale algo.")
        audio = recognizer.listen(source)

    with open(filename, "wb") as file:
        file.write(audio.get_wav_data())
    print(f"Áudio gravado e salvo como {filename}.")
    return filename

def upload_to_s3(filename, bucket_name):
    s3_client.upload_file(filename, bucket_name, filename)
    print(f"Arquivo {filename} enviado para o S3.")

def start_transcription_job(filename, bucket_name):
    job_name = f"transcription-job-{int(time.time())}"
    media_uri = f"s3://{bucket_name}/{filename}"
    
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='pt-BR',
        Media={'MediaFileUri': media_uri},
        MediaFormat='wav',
        OutputBucketName=bucket_name
    )
    print(f"Trabalho de transcrição iniciado para o arquivo {filename}.")
    return job_name

def check_transcription_status(job_name):
    response = transcribe_client.get_transcription_job(
        TranscriptionJobName=job_name
    )
    
    status = response['TranscriptionJob']['TranscriptionJobStatus']
    if status == 'COMPLETED':
        print("Transcrição concluída!")
        return response['TranscriptionJob']['Transcript']['TranscriptFileUri']
    elif status == 'FAILED':
        print("A transcrição falhou.")
        return None
    else:
        print("Transcrição ainda em andamento...")
        return None

if __name__ == "__main__":
    audio_file = record_audio("audio.wav")
    
    upload_to_s3(audio_file, bucket_name)
    
    job_name = start_transcription_job(audio_file, bucket_name)
    
    while True:
        result_uri = check_transcription_status(job_name)
        if result_uri:
            print(f"Transcrição disponível em:\n{result_uri}")
            break
        time.sleep(2)
