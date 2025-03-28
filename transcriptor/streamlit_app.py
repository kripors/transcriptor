# Arquivo principal do Streamlit com correções aplicadas

# Importar o script de inicialização para aplicar as correções
import app_init

# Importar o script de correção do ffmpeg
import ffmpeg_fix

# Ajustar o PATH para encontrar o ffmpeg
ffmpeg_fix.fix_ffmpeg_path()

# Importar o app original
import app