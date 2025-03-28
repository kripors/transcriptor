#!/usr/bin/env python3
"""
Script para baixar versões estáticas do FFmpeg para diferentes sistemas operacionais.
Este script baixa e configura o FFmpeg para ser embutido no aplicativo.
"""

import os
import platform
import shutil
import subprocess
import sys
import zipfile
import tarfile
import urllib.request
from pathlib import Path

FFMPEG_DIR = "ffmpeg_bin"

# URLs para versões estáticas do FFmpeg
FFMPEG_URLS = {
    "Windows": "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip",
    "Linux": "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz",
    "Darwin": "https://evermeet.cx/ffmpeg/getrelease/ffmpeg/zip"  # macOS
}

def ensure_dir(directory):
    """Garante que o diretório existe"""
    os.makedirs(directory, exist_ok=True)
    return directory

def get_current_os():
    """Identifica o sistema operacional atual"""
    system = platform.system()
    if system not in FFMPEG_URLS:
        print(f"Sistema operacional {system} não suportado")
        sys.exit(1)
    return system

def download_file(url, destination):
    """Baixa um arquivo da URL especificada para o destino"""
    print(f"Baixando de {url}...")
    try:
        urllib.request.urlretrieve(url, destination)
        print(f"Download concluído: {destination}")
        return destination
    except Exception as e:
        print(f"Erro ao baixar: {str(e)}")
        return None

def extract_windows_ffmpeg(zip_path, output_dir):
    """Extrai o FFmpeg para Windows do arquivo zip"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    
    # Encontrar o executável ffmpeg.exe e movê-lo para o diretório final
    for root, dirs, files in os.walk(output_dir):
        if "bin" in dirs:
            bin_dir = os.path.join(root, "bin")
            for file in os.listdir(bin_dir):
                if file.endswith(".exe"):
                    src = os.path.join(bin_dir, file)
                    dst = os.path.join(FFMPEG_DIR, file)
                    shutil.copy2(src, dst)
                    print(f"Copiado {file} para {FFMPEG_DIR}")
    
    # Limpar arquivos temporários
    shutil.rmtree(output_dir)

def extract_linux_ffmpeg(tar_path, output_dir):
    """Extrai o FFmpeg para Linux do arquivo tar.xz"""
    with tarfile.open(tar_path, 'r:xz') as tar_ref:
        tar_ref.extractall(output_dir)
    
    # Encontrar o binário ffmpeg e copiá-lo para o diretório final
    for root, dirs, files in os.walk(output_dir):
        if "ffmpeg" in files:
            src = os.path.join(root, "ffmpeg")
            dst = os.path.join(FFMPEG_DIR, "ffmpeg")
            shutil.copy2(src, dst)
            # Tornar o arquivo executável
            os.chmod(dst, 0o755)
            print(f"Copiado ffmpeg para {FFMPEG_DIR}")
        if "ffprobe" in files:
            src = os.path.join(root, "ffprobe")
            dst = os.path.join(FFMPEG_DIR, "ffprobe")
            shutil.copy2(src, dst)
            # Tornar o arquivo executável
            os.chmod(dst, 0o755)
            print(f"Copiado ffprobe para {FFMPEG_DIR}")
    
    # Limpar arquivos temporários
    shutil.rmtree(output_dir)

def extract_macos_ffmpeg(zip_path, output_dir):
    """Extrai o FFmpeg para macOS do arquivo zip"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    
    # Copiar o binário ffmpeg para o diretório final
    for file in os.listdir(output_dir):
        if file.startswith("ffmpeg"):
            src = os.path.join(output_dir, file)
            dst = os.path.join(FFMPEG_DIR, "ffmpeg")
            shutil.copy2(src, dst)
            # Tornar o arquivo executável
            os.chmod(dst, 0o755)
            print(f"Copiado ffmpeg para {FFMPEG_DIR}")
    
    # Limpar arquivos temporários
    shutil.rmtree(output_dir)

def download_ffmpeg_for_current_os():
    """Baixa o FFmpeg para o sistema operacional atual"""
    os_name = get_current_os()
    url = FFMPEG_URLS[os_name]
    temp_dir = ensure_dir(os.path.join("temp", os_name))
    
    print(f"Baixando FFmpeg para {os_name}...")
    
    # Criar diretório para os binários do FFmpeg
    ensure_dir(FFMPEG_DIR)
    
    if os_name == "Windows":
        zip_path = os.path.join(temp_dir, "ffmpeg.zip")
        download_file(url, zip_path)
        extract_windows_ffmpeg(zip_path, temp_dir)
    
    elif os_name == "Linux":
        tar_path = os.path.join(temp_dir, "ffmpeg.tar.xz")
        download_file(url, tar_path)
        extract_linux_ffmpeg(tar_path, temp_dir)
    
    elif os_name == "Darwin":  # macOS
        zip_path = os.path.join(temp_dir, "ffmpeg.zip")
        download_file(url, zip_path)
        extract_macos_ffmpeg(zip_path, temp_dir)

def download_all_ffmpeg():
    """Baixa o FFmpeg para todos os sistemas operacionais suportados"""
    # Criar diretório para os binários do FFmpeg
    ensure_dir(FFMPEG_DIR)
    
    for os_name, url in FFMPEG_URLS.items():
        temp_dir = ensure_dir(os.path.join("temp", os_name))
        
        print(f"Baixando FFmpeg para {os_name}...")
        
        if os_name == "Windows":
            zip_path = os.path.join(temp_dir, "ffmpeg.zip")
            if download_file(url, zip_path):
                extract_windows_ffmpeg(zip_path, temp_dir)
        
        elif os_name == "Linux":
            tar_path = os.path.join(temp_dir, "ffmpeg.tar.xz")
            if download_file(url, tar_path):
                extract_linux_ffmpeg(tar_path, temp_dir)
        
        elif os_name == "Darwin":  # macOS
            zip_path = os.path.join(temp_dir, "ffmpeg.zip")
            if download_file(url, zip_path):
                extract_macos_ffmpeg(zip_path, temp_dir)

def show_help():
    """Mostra ajuda sobre o uso do script"""
    print("Uso: python download_ffmpeg.py [opção]")
    print("Opções:")
    print("  --help      : Mostra esta mensagem de ajuda")
    print("  --current   : Baixa apenas o FFmpeg para o sistema operacional atual (padrão)")
    print("  --all       : Baixa o FFmpeg para todos os sistemas operacionais suportados")
    print("  --windows   : Baixa apenas o FFmpeg para Windows")
    print("  --linux     : Baixa apenas o FFmpeg para Linux")
    print("  --macos     : Baixa apenas o FFmpeg para macOS")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        option = sys.argv[1].lower()
        
        if option == "--help":
            show_help()
        elif option == "--all":
            download_all_ffmpeg()
        elif option == "--windows":
            ensure_dir(FFMPEG_DIR)
            temp_dir = ensure_dir(os.path.join("temp", "Windows"))
            zip_path = os.path.join(temp_dir, "ffmpeg.zip")
            if download_file(FFMPEG_URLS["Windows"], zip_path):
                extract_windows_ffmpeg(zip_path, temp_dir)
        elif option == "--linux":
            ensure_dir(FFMPEG_DIR)
            temp_dir = ensure_dir(os.path.join("temp", "Linux"))
            tar_path = os.path.join(temp_dir, "ffmpeg.tar.xz")
            if download_file(FFMPEG_URLS["Linux"], tar_path):
                extract_linux_ffmpeg(tar_path, temp_dir)
        elif option == "--macos":
            ensure_dir(FFMPEG_DIR)
            temp_dir = ensure_dir(os.path.join("temp", "Darwin"))
            zip_path = os.path.join(temp_dir, "ffmpeg.zip")
            if download_file(FFMPEG_URLS["Darwin"], zip_path):
                extract_macos_ffmpeg(zip_path, temp_dir)
        else:
            print(f"Opção desconhecida: {option}")
            show_help()
    else:
        # Por padrão, baixar apenas para o sistema operacional atual
        download_ffmpeg_for_current_os() 