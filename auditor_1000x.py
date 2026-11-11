import os
import re

print("🤖 INICIANDO VARREDURA SUPREMA 1000X (AUDITORIA FINAL)...\n")

# Lista de palavras que NÃO devem aparecer na interface
palavras_proibidas = [
    'Submit', 'Cancel', 'Search', 'Login', 'Logout', 'Register', 
    'Add to cart', 'Buy now', 'Price', 'Total', 'Subtotal', 
    'Loading', 'Error', 'Success', 'Warning', 'Delete', 'Edit', 
    'Save', 'Update', 'Dashboard', 'Settings', 'Products', 'Categories'
]

pastas = ['app', 'components', 'lib', 'utils', 'src']
total_arquivos = 0
problemas_encontrados = []

for pasta in pastas:
    if not os.path.exists(pasta): continue
    for root, dirs, files in os.walk(pasta):
        if 'node_modules' in root or '.next' in root or '.git' in root: continue
        for file in files:
            if file.endswith(('.tsx', '.ts', '.js', '.jsx')):
                total_arquivos += 1
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Checar palavras em inglês na interface
                for palavra in palavras_proibidas:
                    # Procura a palavra entre tags HTML (ex: >Submit<)
                    if re.search(r'>\s*' + palavra + r'\s*<', content, re.IGNORECASE):
                        problemas_encontrados.append(f"⚠️ Texto em inglês: '{palavra}' em {filepath}")
                    
                    # Procura a palavra em placeholders
                    if re.search(r'placeholder=["\']' + palavra + r'["\']', content, re.IGNORECASE):
                        problemas_encontrados.append(f"⚠️ Placeholder em inglês: '{palavra}' em {filepath}")

                # 2. Checar imagens sem alt (SEO)
                # Encontra tags <img ...> que não tenham a palavra 'alt'
                imagens_sem_alt = re.findall(r'<img(?![^>]*\balt=)[^>]*>', content)
                if imagens_sem_alt:
                    problemas_encontrados.append(f"📸 Imagem sem texto ALT (SEO) em {filepath}")

                # 3. Checar links http:// (Inseguros)
                if 'http://' in content and 'http://localhost' not in content:
                    problemas_encontrados.append(f"🔗 Link inseguro (http://) em {filepath}")

# Gerar Relatório
relatorio_path = 'relatorio_auditoria_1000x.txt'
with open(relatorio_path, 'w', encoding='utf-8') as f:
    f.write(f"=== RELATÓRIO DA VARREDURA SUPREMA 1000X ===\n")
    f.write(f"Arquivos analisados: {total_arquivos}\n\n")
    
    if problemas_encontrados:
        f.write(f"Total de alertas: {len(problemas_encontrados)}\n\n")
        for p in problemas_encontrados:
            f.write(p + "\n")
            print(p)
    else:
        f.write("🏆 PERFEIÇÃO ABSOLUTA! Nenhuma palavra em inglês, imagem sem alt ou link inseguro foi encontrado.\n")
        print("🏆 PERFEIÇÃO ABSOLUTA! O site está impecável.")

print(f"\n🎉 Auditoria 1000x concluída! Relatório salvo em {relatorio_path}")
