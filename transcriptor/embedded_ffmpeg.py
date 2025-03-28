"""
Módulo para gerenciar o FFmpeg embutido no aplicativo.
Este módulo detecta e configura o FFmpeg embutido, independente do sistema operacional.
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path

class EmbeddedFFmpeg:
    """Classe para gerenciar o FFmpeg embutido no aplicativo."""
    
    @staticmethod
    def get_ffmpeg_path():
        """
        Retorna o caminho para o executável FFmpeg embutido.
        
        Returns:
            str: Caminho para o executável FFmpeg ou None se não encontrado
        """
        # Obter o diretório do script atual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Diretório onde estão os binários do FFmpeg
        ffmpeg_dir = os.path.join(script_dir, "ffmpeg_bin")
        
        # Nome do executável, dependendo do sistema operacional
        system = platform.system()
        if system == "Windows":
            ffmpeg_exe = "ffmpeg.exe"
        else:
            ffmpeg_exe = "ffmpeg"
        
        # Caminho completo para o executável
        ffmpeg_path = os.path.join(ffmpeg_dir, ffmpeg_exe)
        
        # Verificar se o executável existe
        if os.path.exists(ffmpeg_path):
            return ffmpeg_path
        
        # Se não encontrou, tentar baixar
        print(f"FFmpeg não encontrado em {ffmpeg_path}. Tentando baixar...")
        
        try:
            # Tentar importar e executar o script de download
            from download_ffmpeg import download_ffmpeg_for_current_os
            download_ffmpeg_for_current_os()
            
            # Verificar novamente se o executável existe
            if os.path.exists(ffmpeg_path):
                return ffmpeg_path
            else:
                print("Não foi possível baixar o FFmpeg.")
                return None
        except Exception as e:
            print(f"Erro ao baixar o FFmpeg: {str(e)}")
            return None
    
    @staticmethod
    def extract_audio(video_path, output_path):
        """
        Extrai áudio de um arquivo de vídeo usando o FFmpeg embutido.
        
        Args:
            video_path (str): Caminho para o arquivo de vídeo
            output_path (str): Caminho para salvar o arquivo de áudio
            
        Returns:
            str: Caminho para o arquivo de áudio ou None em caso de erro
        """
        try:
            # Obter o caminho para o FFmpeg
            ffmpeg_path = EmbeddedFFmpeg.get_ffmpeg_path()
            if not ffmpeg_path:
                print("FFmpeg não encontrado. Não é possível extrair áudio.")
                return None
            
            # Comando para extrair áudio
            command = [
                ffmpeg_path,
                "-i", video_path,
                "-vn",  # Desativa o vídeo
                "-acodec", "libmp3lame",  # Usar codec MP3
                "-q:a", "2",  # Qualidade do áudio (0-9, onde 0 é a melhor)
                "-y",  # Sobrescrever arquivo se existir
                output_path
            ]
            
            # Executar o comando
            process = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Verificar se o arquivo foi criado
            if os.path.exists(output_path):
                return output_path
            else:
                print(f"Arquivo de áudio não foi criado: {output_path}")
                print(f"Saída do FFmpeg: {process.stderr}")
                return None
        
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar FFmpeg: {str(e)}")
            print(f"Saída de erro: {e.stderr}")
            return None
        
        except Exception as e:
            print(f"Erro ao extrair áudio: {str(e)}")
            return None
    
    @staticmethod
    def convert_video(input_path, output_path, options=None):
        """
        Converte um vídeo usando o FFmpeg embutido.
        
        Args:
            input_path (str): Caminho para o arquivo de entrada
            output_path (str): Caminho para salvar o arquivo de saída
            options (dict, optional): Opções adicionais para a conversão
            
        Returns:
            str: Caminho para o arquivo convertido ou None em caso de erro
        """
        try:
            # Obter o caminho para o FFmpeg
            ffmpeg_path = EmbeddedFFmpeg.get_ffmpeg_path()
            if not ffmpeg_path:
                print("FFmpeg não encontrado. Não é possível converter vídeo.")
                return None
            
            # Comando base
            command = [ffmpeg_path, "-i", input_path]
            
            # Adicionar opções específicas
            if options:
                for key, value in options.items():
                    command.append(f"-{key}")
                    if value is not None:
                        command.append(str(value))
            
            # Adicionar saída e opção para sobrescrever
            command.extend(["-y", output_path])
            
            # Executar o comando
            process = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Verificar se o arquivo foi criado
            if os.path.exists(output_path):
                return output_path
            else:
                print(f"Arquivo convertido não foi criado: {output_path}")
                print(f"Saída do FFmpeg: {process.stderr}")
                return None
        
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar FFmpeg: {str(e)}")
            print(f"Saída de erro: {e.stderr}")
            return None
        
        except Exception as e:
            print(f"Erro ao converter vídeo: {str(e)}")
            return None

# Função auxiliar para verificar se o FFmpeg está disponível
def check_ffmpeg():
    """
    Verifica se o FFmpeg embutido está disponível.
    
    Returns:
        bool: True se FFmpeg está disponível, False caso contrário
    """
    ffmpeg_path = EmbeddedFFmpeg.get_ffmpeg_path()
    if ffmpeg_path:
        print(f"FFmpeg encontrado em: {ffmpeg_path}")
        return True
    else:
        print("FFmpeg não encontrado. Algumas funcionalidades podem não estar disponíveis.")
        return False

# Execução direta para teste
if __name__ == "__main__":
    if check_ffmpeg():
        print("FFmpeg embutido está disponível!")
    else:
        print("FFmpeg embutido não está disponível.") 