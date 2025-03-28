# Script para corrigir os problemas de escape sequences no pydub
# Este script deve ser executado antes de iniciar o aplicativo

import re
import os
import sys
from pathlib import Path

def fix_pydub_regex():
    """Corrige as expressões regulares no arquivo pydub/utils.py"""
    try:
        # Encontrar o caminho do módulo pydub
        import pydub
        pydub_path = Path(pydub.__file__).parent
        utils_path = pydub_path / 'utils.py'
        
        if not utils_path.exists():
            print(f"Arquivo não encontrado: {utils_path}")
            return False
        
        # Ler o conteúdo do arquivo
        with open(utils_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Corrigir as expressões regulares
        # Substituir \( por \(
        content = content.replace("'([su]([0-9]{1,2})p?) \(([0-9]{1,2}) bit\)$'", "'([su]([0-9]{1,2})p?) \\(([0-9]{1,2}) bit\\)$'")
        content = content.replace("'([su]([0-9]{1,2})p?)( \(default\))?$'", "'([su]([0-9]{1,2})p?)( \\(default\\))?$'")
        content = content.replace("'(flt)p?( \(default\))?$'", "'(flt)p?( \\(default\\))?$'")
        content = content.replace("'(dbl)p?( \(default\))?$'", "'(dbl)p?( \\(default\\))?$'")
        
        # Escrever o conteúdo corrigido de volta ao arquivo
        with open(utils_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Expressões regulares corrigidas em {utils_path}")
        return True
    except Exception as e:
        print(f"Erro ao corrigir expressões regulares: {str(e)}")
        return False

if __name__ == "__main__":
    fix_pydub_regex()