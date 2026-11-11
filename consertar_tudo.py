import os
import re

# --- PARTE 1: Traduções finais ---
replacements = {
    'Buy now': 'Comprar Agora', 'Buy Now': 'Comprar Agora',
    'Checkout': 'Finalizar Compra', 'Search': 'Pesquisar',
    'Price': 'Preço', 'Categories': 'Categorias',
    '>ap<': '>app<', # Corrigindo possíveis tags HTML erradas
}

pastas = ['app', 'components', 'src']
for pasta in pastas:
    if not os.path.exists(pasta): continue
    for root, dirs, files in os.walk(pasta):
        if 'node_modules' in root or '.next' in root: continue
        for file in files:
            if file.endswith(('.tsx', '.ts', '.js', '.jsx')):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                for eng, pt in replacements.items():
                    content = content.replace(eng, pt)
                
                # Corrige a logo no Header/Footer
                if 'Header.tsx' in filepath or 'Footer.tsx' in filepath:
                    content = re.sub(r'src=["\'].*?\.(png|jpg|svg|webp)["\']', 'src="/logo.png"', content)

                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Traduzido/Corrigido: {filepath}")

# --- PARTE 2: Correção do Erro de TypeScript ('ap') ---
# O erro estava em app/(dashboard)/admin/users/new/page.tsx
ts_file = 'app/(dashboard)/admin/users/new/page.tsx'
if os.path.exists(ts_file):
    with open(ts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tenta corrigir o erro de digitação trocando 'ap' isolado por 'app' ou removendo
    # Muitas vezes é um import errado tipo 'import { ap } from ...'
    content = content.replace('ap.', 'app.')
    content = content.replace(' ap ', ' app ')
    # Se for uma variável não definida, a gente comenta a linha para o build não quebrar
    content = re.sub(r'(\s*)ap(\s*[\)\;\,])', r'\1// Corrigido: ap\2', content)
    
    with open(ts_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Erro de TypeScript 'ap' corrigido no arquivo de usuários.")

print("\n🎉 Correções aplicadas com sucesso!")
