import os
import glob

# Procura todos os arquivos route.ts dentro da pasta app/api
for filepath in glob.glob('app/api/**/route.ts', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "export const dynamic = 'force-dynamic';" not in content:
        # Adiciona no topo do arquivo
        new_content = "export const dynamic = 'force-dynamic';\n\n" + content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'✅ Dinâmico adicionado em: {filepath}')
