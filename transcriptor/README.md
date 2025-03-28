# Processador de Áudio e Transcrição

Aplicativo Streamlit para processamento de áudio, transcrição e geração de resumos profissionais.

## Funcionalidades

- Upload e extração de áudio de vídeos
- Transcrição automática usando API Groq
- Geração de resumos profissionais com Google Gemini
- Conversão para documentos formatados DOCX

## Deploy no Streamlit Cloud

Para fazer deploy no Streamlit Cloud:

1. Faça login em [streamlit.io](https://streamlit.io)
2. Crie um novo app apontando para este repositório
3. Adicione as seguintes secrets:
   - `GROQ_API_KEY`: Sua chave de API do Groq
   - `GOOGLE_API_KEY`: Sua chave de API do Google Gemini

## Configuração Local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requisitos

- Python 3.9+
- FFmpeg (instalado automaticamente no Streamlit Cloud)
- Chaves de API para Groq e Google Gemini

## Arquivos de Configuração

- `requirements.txt`: Dependências Python
- `packages.txt`: Dependências de sistema
- `nltk.txt`: Recursos NLTK
- `.streamlit/config.toml`: Configurações do Streamlit 

## Dependências externas

Este aplicativo utiliza o FFmpeg para processamento de áudio e vídeo. Para sua conveniência, incluímos uma versão embutida do FFmpeg que é baixada automaticamente quando necessário.

### FFmpeg Embutido

O aplicativo inclui um sistema automatizado para baixar e configurar o FFmpeg:

- Quando o aplicativo for iniciado pela primeira vez, ele detectará automaticamente o sistema operacional e baixará a versão adequada do FFmpeg.
- Os binários do FFmpeg serão armazenados localmente na pasta `ffmpeg_bin`.
- Não é necessário instalar o FFmpeg separadamente.

### Download Manual do FFmpeg

Se preferir baixar manualmente o FFmpeg, você pode executar:

```bash
python download_ffmpeg.py
```

Opções disponíveis:
- `--help`: Mostra ajuda sobre o uso do script
- `--current`: Baixa apenas para o sistema operacional atual (padrão)
- `--all`: Baixa para todos os sistemas operacionais suportados (Windows, Linux, macOS)
- `--windows`: Baixa apenas para Windows
- `--linux`: Baixa apenas para Linux
- `--macos`: Baixa apenas para macOS

### Para desenvolvedores

Se estiver desenvolvendo ou modificando este aplicativo, o módulo `embedded_ffmpeg.py` fornece uma API para trabalhar com o FFmpeg embutido:

```python
from embedded_ffmpeg import EmbeddedFFmpeg

# Extrair áudio de um vídeo
EmbeddedFFmpeg.extract_audio("video.mp4", "audio.mp3")

# Converter um vídeo
EmbeddedFFmpeg.convert_video("input.mp4", "output.webm", options={"vcodec": "vp9", "acodec": "opus"})
``` 