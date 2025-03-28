# Arquivo principal do Streamlit com correções aplicadas
import platform
import os
import sys
import streamlit as st

# Configuração da página - DEVE ser a primeira chamada Streamlit
st.set_page_config(
    page_title="Processador de Áudio e Transcrição",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Verificar se o FFmpeg embutido está disponível
try:
    from embedded_ffmpeg import check_ffmpeg
    
    # Verificar se o FFmpeg está disponível
    if check_ffmpeg():
        st.success("FFmpeg embutido encontrado e configurado com sucesso!")
    else:
        # Tentar baixar o FFmpeg
        try:
            from download_ffmpeg import download_ffmpeg_for_current_os
            download_ffmpeg_for_current_os()
            # Verificar novamente
            if check_ffmpeg():
                st.success("FFmpeg baixado e configurado com sucesso!")
            else:
                st.warning("Não foi possível configurar o FFmpeg embutido. Algumas funcionalidades podem não estar disponíveis.")
        except Exception as e:
            st.error(f"Erro ao baixar FFmpeg: {str(e)}")
except ImportError:
    st.warning("Módulo de FFmpeg embutido não encontrado. Continuando com o método padrão.")

# Para Windows, verificar se o ffmpeg está instalado
system = platform.system()
if system == "Windows":
    try:
        # Importar o script de instalação do ffmpeg para Windows
        import windows_ffmpeg_installer
        windows_ffmpeg_installer.install_ffmpeg()
    except ImportError:
        print("Não foi possível importar o script de instalação do ffmpeg para Windows")
    except Exception as e:
        print(f"Erro ao tentar instalar ffmpeg: {str(e)}")

# Para Linux/Mac, executar o script de configuração
else:
    try:
        # No Streamlit Cloud, o script setup.sh não pode ser executado diretamente
        # Mas podemos verificar e configurar o PATH para ffmpeg
        os.environ["PATH"] = os.environ["PATH"] + os.pathsep + "/usr/bin" + os.pathsep + "/usr/local/bin" + os.pathsep + "/app/.apt/usr/bin" + os.pathsep + "/home/appuser/.apt/usr/bin"
    except Exception as e:
        print(f"Erro ao configurar o PATH: {str(e)}")

# Importar o script de inicialização para aplicar as correções
import app_init

# Importar o script de correção do ffmpeg
import ffmpeg_fix

# Ajustar o PATH para encontrar o ffmpeg
ffmpeg_encontrado = ffmpeg_fix.fix_ffmpeg_path()

if not ffmpeg_encontrado:
    st.warning("FFmpeg não encontrado no sistema. Usando a versão embutida.")

# Importar o app original
import app

# Substituir a função set_page_config no módulo app para não fazer nada
# Isso é necessário para evitar chamadas duplicadas
app.st.set_page_config = lambda **kwargs: None