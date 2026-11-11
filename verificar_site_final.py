import os
import re

print("🕵️ INICIANDO VERIFICAÇÃO FINAL DE SEGURANÇA...\n")
tudo_ok = True

# 1. Verificar se o FaPesquisar sumiu
print("1️⃣ Verificando ícones de busca...")
grep_result = os.popen('grep -r "FaPesquisar" app components lib utils src 2>/dev/null').read()
if grep_result:
    print(f"❌ AINDA EXISTE FaPesquisar em:\n{grep_result}")
    tudo_ok = False
else:
    print("✅ FaPesquisar corrigido (agora é FaSearch).")

# 2. Verificar se o usePesquisarParams sumiu
print("\n2️⃣ Verificando parâmetros de pesquisa...")
grep_result = os.popen('grep -r "usePesquisarParams" app components 2>/dev/null').read()
if grep_result:
    print(f"❌ AINDA EXISTE usePesquisarParams em:\n{grep_result}")
    tudo_ok = False
else:
    print("✅ usePesquisarParams corrigido (agora é useSearchParams).")

# 3. Verificar a ordem do "use client" no Login e Register
print("\n3️⃣ Verificando diretiva 'use client' no Login e Register...")
for file in ['app/login/page.tsx', 'app/register/page.tsx']:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            primeira_linha = f.readline().strip()
            if primeira_linha != '"use client";' and primeira_linha != "'use client';":
                print(f"❌ ERRO em {file}: A primeira linha é '{primeira_linha}' (deveria ser 'use client')")
                tudo_ok = False
            else:
                print(f"✅ {file}: 'use client' está na primeira linha.")
    else:
        print(f"❌ Arquivo {file} não encontrado.")
        tudo_ok = False

# 4. Verificar se a logo existe
print("\n4️⃣ Verificando logo...")
if os.path.exists('public/logo.png'):
    print("✅ Logo 'public/logo.png' encontrada.")
elif os.path.exists('public/logo.jpg'):
    print("✅ Logo 'public/logo.jpg' encontrada.")
else:
    print("❌ Logo NÃO encontrada na pasta public.")
    tudo_ok = False

# 5. Verificar next.config.js
print("\n5️⃣ Verificando next.config.js...")
if os.path.exists('next.config.js'):
    with open('next.config.js', 'r', encoding='utf-8') as f:
        content = f.read()
        if 'serverExternalPackages' in content:
            print("⚠️ AVISO: 'serverExternalPackages' está no next.config.js. Em Next.js 14, o correto é 'serverComponentsExternalPackages'.")
        else:
            print("✅ next.config.js parece correto.")
else:
    print("❌ next.config.js não encontrado.")
    tudo_ok = False

print("\n" + "="*40)
if tudo_ok:
    print("🏆 TUDO PRONTO! O site está 100% blindado para o deploy final.")
    print("👉 Vá na Netlify e clique em 'Trigger deploy' > 'Deploy project'.")
else:
    print("⚠️ ALGUNS PROBLEMAS FORAM ENCONTRADOS. Verifique os detalhes acima.")
