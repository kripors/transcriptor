# Script de inicialização para corrigir problemas antes de iniciar o aplicativo

import os
import sys
import subprocess

# Adicionar o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar os scripts de correção
from pydub_fix import fix_pydub_regex
from fix_empty_label import fix_streamlit_app

# Executar as correções
print("Aplicando correções para o Streamlit Cloud...")

# Corrigir as expressões regulares no pydub
print("Corrigindo expressões regulares no pydub...")
fix_pydub_regex()

# Corrigir os labels vazios no app.py
print("Corrigindo labels vazios no app.py...")
fix_streamlit_app()

# Verificar se o ffmpeg está instalado
print("Verificando instalação do ffmpeg...")
try:
    result = subprocess.run(['which', 'ffmpeg'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"FFmpeg encontrado em: {result.stdout.strip()}")
    else:
        print("FFmpeg não encontrado no PATH. Verifique se está instalado corretamente.")
        print("O arquivo packages.txt deve conter 'ffmpeg' para instalação no Streamlit Cloud.")
except Exception as e:
    print(f"Erro ao verificar ffmpeg: {str(e)}")

print("Correções aplicadas com sucesso!")