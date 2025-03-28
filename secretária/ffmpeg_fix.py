# Script para ajudar a encontrar o ffmpeg no Streamlit Cloud
import os
import sys
import subprocess
import shutil

def fix_ffmpeg_path():
    """Ajusta o PATH para incluir diretórios adicionais onde o ffmpeg pode estar instalado no Streamlit Cloud"""
    print("Ajustando PATH para encontrar o ffmpeg...")
    
    # Adicionar diretórios comuns onde o ffmpeg pode estar instalado no Streamlit Cloud
    additional_paths = [
        "/usr/bin",
        "/usr/local/bin",
        "/app/.apt/usr/bin",  # Caminho específico do Streamlit Cloud
        "/home/appuser/.apt/usr/bin"  # Outro caminho possível no Streamlit Cloud
    ]
    
    # Adicionar os caminhos ao PATH
    for path in additional_paths:
        if path not in os.environ["PATH"]:
            os.environ["PATH"] = path + os.pathsep + os.environ["PATH"]
            print(f"Adicionado {path} ao PATH")
    
    # Verificar se o ffmpeg está disponível após ajustar o PATH
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path:
        print(f"FFmpeg encontrado em: {ffmpeg_path}")
        return True
    else:
        print("FFmpeg não encontrado mesmo após ajustar o PATH")
        return False

if __name__ == "__main__":
    fix_ffmpeg_path()