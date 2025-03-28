#!/bin/bash

# Script para verificar e configurar o ffmpeg no ambiente Streamlit Cloud

echo "Verificando instalação do ffmpeg..."

# Verificar se ffmpeg está instalado
if command -v ffmpeg >/dev/null 2>&1; then
    echo "FFmpeg encontrado no sistema"
    ffmpeg -version
else
    echo "FFmpeg não encontrado, verificando o diretório de instalação"
    # No Streamlit Cloud, o ffmpeg pode estar em um local diferente
    export PATH="$PATH:/usr/bin:/usr/local/bin:/app/.apt/usr/bin"
    
    if command -v ffmpeg >/dev/null 2>&1; then
        echo "FFmpeg encontrado após ajuste do PATH"
        ffmpeg -version
    else
        echo "FFmpeg não encontrado mesmo após ajuste do PATH"
        echo "Tentando instalar ffmpeg manualmente..."
        apt-get update && apt-get install -y ffmpeg
    fi
fi

echo "Configuração concluída"