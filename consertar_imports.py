import os
import re

# Recria o route.ts com o formato correto para Next.js 15
route_path = 'app/api/auth/[...nextauth]/route.ts'
os.makedirs(os.path.dirname(route_path), exist_ok=True)
with open(route_path, 'w', encoding='utf-8') as f:
    f.write('''import NextAuth from "next-auth";
import authOptions from "@/lib/authOptions";

const handler = NextAuth(authOptions);

export const GET = handler;
export const POST = handler;
''')
print("✅ route.ts recriado no formato Next.js 15")

# Varre o projeto procurando imports do authOptions no lugar errado
count = 0
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.next' in root:
        continue
    for file in files:
        if file.endswith(('.ts', '.tsx', '.js', '.jsx')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content
            # Substitui imports antigos pelo novo caminho @/lib/authOptions
            content = content.replace('@/app/api/auth/[...nextauth]/route', '@/lib/authOptions')
            content = re.sub(r'from\s+[\'"].*?/api/auth/\[\.\.\.nextauth\]/route[\'"]', 'from "@/lib/authOptions"', content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Import corrigido em: {filepath}")
                count += 1

if count == 0:
    print("ℹ️ Nenhum outro arquivo precisou de correção.")
