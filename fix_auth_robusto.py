import os
import re

route_path = 'app/api/auth/[...nextauth]/route.ts'
lib_dir = 'lib'
auth_options_path = os.path.join(lib_dir, 'authOptions.ts')

if os.path.exists(route_path):
    with open(route_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Procura a declaração do authOptions (com ou sem export, com ou sem tipo)
    match = re.search(r'(export\s+)?const\s+authOptions', content)
    
    if match:
        start_idx = match.start()
        # Encontra a primeira chave '{' após a declaração
        brace_idx = content.find('{', start_idx)
        
        if brace_idx != -1:
            # Conta as chaves para achar o fechamento correto do objeto
            open_braces = 0
            end_idx = -1
            for i in range(brace_idx, len(content)):
                if content[i] == '{':
                    open_braces += 1
                elif content[i] == '}':
                    open_braces -= 1
                    if open_braces == 0:
                        end_idx = i + 1
                        break
            
            if end_idx != -1:
                # Extrai todo o bloco do authOptions
                full_declaration = content[start_idx:end_idx]
                
                # Cria o arquivo na pasta lib
                os.makedirs(lib_dir, exist_ok=True)
                with open(auth_options_path, 'w', encoding='utf-8') as f:
                    # Remove o 'export' e adiciona export default
                    decl = full_declaration.replace('export ', '')
                    f.write("import { AuthOptions } from 'next-auth';\n\n")
                    f.write(decl + "\n\nexport default authOptions;\n")
                
                # Remove o authOptions do route.ts
                new_content = content[:start_idx] + content[end_idx:]
                
                # Adiciona o import no topo do route.ts
                new_content = 'import authOptions from "../../../lib/authOptions";\n' + new_content
                
                # Corrige o export do NextAuth para o padrão do Next.js 14/15
                new_content = re.sub(r'export\s*{\s*handler\s+as\s+GET\s*,\s*handler\s+as\s+POST\s*};?', 'export const GET = handler;\nexport const POST = handler;', new_content)

                with open(route_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print('✅ authOptions movido para lib/authOptions.ts')
                print('✅ route.ts atualizado com sucesso!')
            else:
                print('❌ Erro ao encontrar o fechamento do bloco.')
        else:
            print('❌ Erro ao encontrar a abertura do bloco.')
    else:
        print('❌ Declaração authOptions não encontrada.')
else:
    print('❌ Arquivo route.ts não encontrado.')
