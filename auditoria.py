import os
import re
import subprocess

print("🔍 Iniciando auditoria do código do Zixlima...\n")
relatorio = []

# --- 1. CHECAGEM DA LOGO ---
print("⏳ Verificando logo...")
if os.path.exists('public/logo.png'):
    relatorio.append("✅ Logo: A imagem 'logo.png' está na pasta public.")
else:
    relatorio.append("❌ Logo: A imagem 'logo.png' NÃO FOI ENCONTRADA na pasta public.")

# --- 2. BUSCA POR TEXTOS EM INGLÊS ---
print("⏳ Procurando textos não traduzidos...")
english_words = ['Login', 'Register', 'Search', 'Cart', 'Checkout', 'Price', 'Add to', 'Buy now', 'Home', 'Shop', 'Categories']
encontrados = set()

for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.next' in root: continue
    for file in files:
        if file.endswith('.tsx'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                for word in english_words:
                    # Busca a palavra dentro de tags html (ex: >Login<)
                    if re.search(r'>\s*' + word + r'\s*<', content, re.IGNORECASE):
                        encontrados.add(word)

if encontrados:
    relatorio.append(f"⚠️ Textos em inglês encontrados: {', '.join(encontrados)}")
else:
    relatorio.append("✅ Textos: Nenhum texto em inglês óbvio foi encontrado no front-end.")

# --- 3. CHECAGEM DO TYPESCRIPT (Erros ocultos) ---
print("⏳ Testando TypeScript (pode levar 30 segundos)...")
try:
    # Roda o tsc apenas para ver os erros, sem gerar arquivos
    result = subprocess.run(['npx', 'tsc', '--noEmit'], capture_output=True, text=True, timeout=60)
    if result.stdout or result.stderr:
        erros = result.stdout.split('\n') + result.stderr.split('\n')
        erros_reais = [e for e in erros if 'error TS' in e]
        if erros_reais:
            relatorio.append(f"❌ TypeScript: Encontrados {len(erros_reais)} erros de tipagem.")
            relatorio.append(f"   Exemplo: {erros_reais[0]}")
        else:
            relatorio.append("✅ TypeScript: Nenhum erro de tipagem encontrado.")
    else:
        relatorio.append("✅ TypeScript: Nenhum erro de tipagem encontrado.")
except Exception as e:
    relatorio.append(f"⚠️ TypeScript: Não foi possível rodar a checagem ({e}).")

# --- 4. ARQUIVOS INÚTEIS ---
print("⏳ Verificando arquivos indesejados...")
arquivos_inuteis = ['.env', '.env.local', 'wrangler.jsonc']
for arq in arquivos_inuteis:
    if os.path.exists(arq):
        relatorio.append(f"⚠️ Segurança: O arquivo {arq} ainda está na raiz do projeto (cuidado com segredos).")
    else:
        relatorio.append(f"✅ Segurança: Arquivo {arq} não encontrado (bom!).")

# --- SALVANDO E MOSTRANDO O RELATÓRIO ---
with open('relatorio_zixlima.txt', 'w', encoding='utf-8') as f:
    f.write("=== RELATÓRIO DE AUDITORIA ZIXLIMA ===\n\n")
    for linha in relatorio:
        f.write(linha + "\n")
        print(linha)

print("\n🎉 Auditoria concluída! O relatório foi salvo em 'relatorio_zixlima.txt'.")
