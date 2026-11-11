import os
import re

# Tenta achar o arquivo do rodapé
footer_files = ['components/Footer.tsx', 'components/Footer/index.tsx', 'app/components/Footer.tsx']

for filepath in footer_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Substitui textos remanescentes
        content = content.replace('SINGITRONIC', 'ZIXLIMA')
        content = content.replace('Singitronic', 'Zixlima')
        content = content.replace('singitronic', 'zixlima')
        
        # Tenta trocar a imagem antiga pela sua logo
        content = re.sub(r'src=["\']/.*?\.(png|jpg|svg|webp)["\']', 'src="/logo.jpg"', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Rodapé corrigido: {filepath}")
        break
else:
    print("⚠️ Arquivo do rodapé não encontrado. Usaremos apenas o CSS para esconder a imagem antiga.")
