import os

auth_options_path = 'lib/authOptions.ts'
prisma_file = None

# Procura o arquivo que cria o PrismaClient no projeto
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.next' in root:
        continue
    for file in files:
        if file.endswith(('.ts', '.js', '.tsx', '.jsx')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'new PrismaClient()' in content and 'export' in content:
                    prisma_file = filepath
                    break
    if prisma_file:
        break

with open(auth_options_path, 'r', encoding='utf-8') as f:
    auth_content = f.read()

if prisma_file:
    # Transforma o caminho em um alias para o Next.js (ex: @/lib/prisma)
    rel_path = os.path.relpath(prisma_file, '.').replace('\\', '/')
    rel_path = os.path.splitext(rel_path)[0]
    if rel_path.startswith('src/'):
        rel_path = rel_path[4:]
    alias = f'@/{rel_path}'
    
    print(f'✅ Encontrado PrismaClient em: {prisma_file}')
    print(f'✅ Atualizando import para: {alias}')
    
    auth_content = auth_content.replace('import prisma from "@/lib/prisma";', f'import prisma from "{alias}";')
else:
    print('⚠️ Não foi encontrado um arquivo exportando PrismaClient. Usando o cliente direto para garantir o build.')
    auth_content = auth_content.replace('import prisma from "@/lib/prisma";', 'import { PrismaClient } from "@prisma/client";\nconst prisma = new PrismaClient();')

with open(auth_options_path, 'w', encoding='utf-8') as f:
    f.write(auth_content)
print('✅ Arquivo authOptions.ts atualizado!')
