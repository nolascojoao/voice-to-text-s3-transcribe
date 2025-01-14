# Python 🐍 + Boto3 + S3 + Amazon Transcribe


Script Python para gravar áudio, enviar ao S3 e transcrever com AWS Transcribe.


---


## Requisitos


  - Python 3.6+ instalado.


  - Bucket S3 criado e credenciais AWS configuradas (com permissões para S3 e Transcribe).


  - Instale as dependências: ⚠️
```bash
pip install boto3 pyaudio SpeechRecognition  
```


---


## Como Rodar 🟢


1. Configure `bucket_name` com o nome do seu bucket S3 e `region` com sua região AWS no script `record_and_transcribe.py`
```python
bucket_name = "YOUR_BUCKET_NAME"  # Seu bucket S3
region = "us-east-1"  # Sua região
```


3. Execute o script com: ✅
```bash
python record_and_transcribe.py
```
> A gravação será interrompida automaticamente assim que você parar de falar. ℹ️


#


O script fará o seguinte:


  - Grava o áudio com o microfone e salva como um arquivo .wav.
  
  
  - Envia o arquivo gravado para o seu bucket S3.


  - Inicia o trabalho de transcrição com o AWS Transcribe.


  - Após a conclusão da transcrição, o link para acessar o arquivo transcrito no bucket S3 será exibido.
  > O arquivo transcrito será salvo no bucket S3 no formato `.json`. ℹ️


  ---


Saída do terminal após executar o script


<div align="center">
  <img src="https://github.com/user-attachments/assets/48b3c357-ac99-45a0-99c0-b56065461cf4"/>
</div>
  
