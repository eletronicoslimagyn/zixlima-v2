import os
import glob

# Procura por pages e layouts
for filepath in glob.glob('app/**/page.tsx', recursive=True) + glob.glob('app/**/layout.tsx', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    content_str = "".join(lines)
    # Verifica se o arquivo usa hooks do React
    needs_client = any(hook in content_str for hook in ['useState', 'useEffect', 'use(', 'useRouter', 'usePathname', 'useRef'])

    new_lines = []
    skip_header = True
    
    for line in lines:
        stripped = line.strip()
        if skip_header:
            # Ignora as diretivas antigas e linhas vazias no topo
            if stripped in ['"use client";', "'use client';", 'export const dynamic = "force-dynamic";', "export const dynamic = 'force-dynamic';", ''] or stripped.startswith('//'):
                continue
            else:
                skip_header = False
        new_lines.append(line)

    # Monta o topo do arquivo na ordem correta
    header = []
    if needs_client:
        header.append('"use client";\n')
    header.append('export const dynamic = "force-dynamic";\n\n')

    final_content = "".join(header) + "".join(new_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"✅ Corrigido: {filepath}")
