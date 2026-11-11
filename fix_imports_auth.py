path = 'lib/authOptions.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

imports = []
# Verifica se os imports necessários já existem, se não, adiciona
if 'CredentialsProvider' in content and 'import CredentialsProvider' not in content:
    imports.append('import CredentialsProvider from "next-auth/providers/credentials";')
    
if 'PrismaAdapter' in content and 'import { PrismaAdapter }' not in content:
    imports.append('import { PrismaAdapter } from "@auth/prisma-adapter";')

if 'prisma' in content and 'import prisma' not in content and 'import { prisma }' not in content:
    imports.append('import prisma from "@/lib/prisma";')

if imports:
    # Adiciona os imports no topo do arquivo
    new_content = '\n'.join(imports) + '\n' + content
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('✅ Imports adicionados:', imports)
else:
    print('ℹ️ Imports já estavam corretos.')
