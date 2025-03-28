# Script para corrigir o problema de label vazio no Streamlit

def fix_streamlit_app():
    """Modifica o app.py para corrigir o problema de label vazio"""
    try:
        import os
        from pathlib import Path
        
        # Caminho do arquivo app.py
        app_path = Path(os.path.dirname(os.path.abspath(__file__))) / 'app.py'
        
        if not app_path.exists():
            print(f"Arquivo não encontrado: {app_path}")
            return False
        
        # Ler o conteúdo do arquivo
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procurar por file_uploader com label vazio
        if 'video_file = st.file_uploader("", type=[' in content:
            # Substituir o label vazio por um label não vazio
            content = content.replace(
                'video_file = st.file_uploader("", type=[',
                'video_file = st.file_uploader("Selecione um arquivo de vídeo", type=[')
        
        # Procurar por outros componentes com label vazio
        # Verificar text_area com label vazio
        if 'st.text_area("", ' in content:
            content = content.replace(
                'st.text_area("", ',
                'st.text_area("Texto", ')
        
        # Escrever o conteúdo modificado de volta ao arquivo
        with open(app_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Labels vazios corrigidos em {app_path}")
        return True
    except Exception as e:
        print(f"Erro ao corrigir labels vazios: {str(e)}")
        return False

if __name__ == "__main__":
    fix_streamlit_app()