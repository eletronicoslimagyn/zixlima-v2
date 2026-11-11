import os
import re

route_path = 'app/api/auth/[...nextauth]/route.ts'
lib_dir = 'lib'
auth_options_path = os.path.join(lib_dir, 'authOptions.ts')

if os.path.exists(route_path):
    with open(route_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Procura o bloco do authOptions
    match = re.search(r'export const authOptions\s*=\s*({[\s\S]*?});', content)
    
    if match:
        # 1. Extrai o objeto authOptions
        auth_options_content = match.group(0).replace('export const', 'const')
        auth_options_content += '\nexport default authOptions;\n'

        # Cria a pasta lib
        os.makedirs(lib_dir, exist_ok=True)

        # 2. Salva o authOptions no arquivo novo
        with open(auth_options_path, 'w', encoding='utf-8') as f:
            f.write(auth_options_content)

        # 3. Remove o authOptions do route.ts e adiciona o import
        new_content = content.replace(match.group(0), '')
        import_line = 'import authOptions from "../../../lib/authOptions";\n'
        
        # Adiciona o import no topo
        new_content = import_line + new_content
        
        # 4. Corrige o export final do NextAuth
        new_content = re.sub(r'export\s*{\s*handler\s+as\s+GET\s*,\s*handler\s+as\s+POST\s*};?', 'export const GET = handler;\nexport const POST = handler;', new_content)

        with open(route_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print('✅ authOptions movido para lib/authOptions.ts')
        print('✅ route.ts atualizado corretamente!')
    else:
        print('❌ Não foi possível encontrar o authOptions no route.ts')
else:
    print('❌ Arquivo route.ts não encontrado')
