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