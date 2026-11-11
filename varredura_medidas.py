import os
import re

print("📏 INICIANDO VARREDURA SUPREMA 1: ADEQUAÇÃO DE MEDIDAS (RESPONSIVIDADE)\n")

# --- PARTE 1: Redes de segurança globais no CSS ---
css_path = 'app/globals.css'
if os.path.exists(css_path):
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("""
/* --- ZIXLIMA SUPREME RESPONSIVENESS FIX --- */
html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
}
img, video, iframe {
    max-width: 100% !important;
    height: auto !important;
}
""")
    print("✅ Regras globais de proteção de tela (overflow e imagens) injetadas no CSS!")

# --- PARTE 2: Varredura nos componentes para arrumar tags <img> ---
pastas = ['app', 'components', 'src']
imagens_ajustadas = 0

for pasta in pastas:
    if not os.path.exists(pasta): continue
    for root, dirs, files in os.walk(pasta):
        if 'node_modules' in root or '.next' in root: continue
        for file in files:
            if file.endswith(('.tsx', '.jsx')):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original = content

                # Se tiver tag <img> antiga, adiciona classes de responsividade se não existirem
                def fix_img_tag(match):
                    full_tag = match.group(0)
                    # Se já tem w-full ou max-w-full, ignora
                    if 'w-full' in full_tag or 'max-w-full' in full_tag or 'w-32' in full_tag or 'w-40' in full_tag:
                        return full_tag
                    # Se tem className, injeta as classes lá dentro
                    if 'className=' in full_tag:
                        return re.sub(r'className=["\'](.*?)["\']', r'className="\1 max-w-full h-auto"', full_tag)
                    # Se não tem className, cria uma
                    else:
                        return full_tag.replace('<img', '<img className="max-w-full h-auto"')

                # Aplica a correção em tags <img>
                content = re.sub(r'<img[^>]*>', fix_img_tag, content)

                # Remove larguras fixas muito grandes (ex: width="800") que quebram no celular
                content = re.sub(r'width=["\'](\d{3,})["\']', 'width="100%"', content)
                content = re.sub(r'height=["\'](\d{3,})["\']', 'height="auto"', content)

                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"📱 Medidas ajustadas em: {filepath}")
                    imagens_ajustadas += 1

print(f"\n🎉 Varredura Suprema 1 concluída! {imagens_ajustadas} componentes ajustados para mobile/desktop.")
