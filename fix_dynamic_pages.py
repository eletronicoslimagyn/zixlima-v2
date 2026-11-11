import os
import glob

# Pega todos os arquivos page.tsx do projeto
for filepath in glob.glob('app/**/page.tsx', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "export const dynamic = 'force-dynamic';" not in content:
        # Adiciona a configuração no topo do arquivo
        new_content = "export const dynamic = 'force-dynamic';\n\n" + content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'✅ Dinâmico adicionado em: {filepath}')
