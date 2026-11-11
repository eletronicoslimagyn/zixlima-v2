import os

files = ['app/login/page.tsx', 'app/register/page.tsx']

for filepath in files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    has_use_client = False
    has_fa_eye = False

    # Limpa o topo do arquivo
    for line in lines:
        stripped = line.strip()
        if stripped in ['"use client";', "'use client';"]:
            has_use_client = True
            continue
        if 'import { FaEye, FaEyeSlash }' in stripped:
            has_fa_eye = True
            continue
        if 'export const dynamic' in stripped:
            continue
        new_lines.append(line)

    # Reconstrói o topo na ordem correta
    header = []
    header.append('"use client";\n')
    header.append('export const dynamic = "force-dynamic";\n\n')
    if has_fa_eye:
        header.append('import { FaEye, FaEyeSlash } from "react-icons/fa";\n')

    final_content = "".join(header) + "".join(new_lines)
    
    # Conserta o erro de digitação da tradução anterior
    final_content = final_content.replace('usePesquisarParams', 'useSearchParams')
    final_content = final_content.replace('PesquisarParams', 'SearchParams')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ Diretivas corrigidas em: {filepath}")

print("🎉 Tudo pronto para o build!")
