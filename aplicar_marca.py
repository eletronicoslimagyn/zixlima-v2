import os
import re

# --- PARTE 1: Trocar os textos em todo o projeto ---
ignore_dirs = ['node_modules', '.git', '.next', '.netlify']
replacements = {
    'SINGITRONIC': 'ZIXLIMA',
    'Singitronic': 'Zixlima',
    'singitronic': 'zixlima',
    'ELECTRONIC ECOMMERCE': 'ELETRÔNICOS',
    'Electronic Ecommerce': 'Eletrônicos',
    'electronic ecommerce': 'eletrônicos'
}

print("⏳ Trocando textos no projeto...")
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith(('.tsx', '.ts', '.js', '.jsx', '.html')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for old, new in replacements.items():
                content = content.replace(old, new)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

# --- PARTE 2: Forçar a logo nova no Header ---
print("⏳ Atualizando a logo no cabeçalho...")
header_path = 'components/Header.tsx'
if os.path.exists(header_path):
    with open(header_path, 'r', encoding='utf-8') as f:
        header_content = f.read()
    
    # Substitui qualquer imagem antiga da logo pela nova
    header_content = re.sub(r'src=["\']/.*?\.(png|jpg|svg|webp)["\']', 'src="/logo.png"', header_content)
    
    with open(header_path, 'w', encoding='utf-8') as f:
        f.write(header_content)
    print("✅ Cabeçalho atualizado!")
else:
    print("⚠️ Arquivo Header.tsx não encontrado, mas os textos foram trocados.")

print("\n🎉 Marca Zixlima Eletrônicos aplicada com sucesso!")
