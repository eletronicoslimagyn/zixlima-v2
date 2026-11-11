import os
import re

replacements = {
    '>Login<': '>Entrar<', '>Register<': '>Cadastrar<', '>Logout<': '>Sair<',
    'Type here': 'O que você procura?', '>Search<': '>Pesquisar<',
    'Home': 'Início', '>Shop<': '>Loja<', 'All products': 'Todos os produtos',
    'Filters': 'Filtros', 'Availability': 'Disponibilidade',
    'In stock': 'Em estoque', 'Out of stock': 'Esgotado', 'Price': 'Preço'
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
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)

footer_path = 'components/Footer.tsx'
if os.path.exists(footer_path):
    with open(footer_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'suporte@zixlima.com.br' not in content:
        email_html = '''
        <div className="w-full text-center mt-6 pt-6 border-t border-gray-700">
            <p className="text-white font-semibold"><i className="fa fa-envelope mr-2"></i> Contato: suporte@zixlima.com.br</p>
        </div>
        '''
        content = content.replace('</footer>', email_html + '\n</footer>')
        with open(footer_path, 'w', encoding='utf-8') as f:
            f.write(content)
    print("✅ Rodapé atualizado!")

with open('app/globals.css', 'a', encoding='utf-8') as f:
    f.write("""
/* --- TAPA NO SELO NETLIFY --- */
#netlify-badge, iframe[src*="netlify"], a[href*="netlify.com"], div[style*="position: fixed"][style*="bottom"] {
    display: none !important; visibility: hidden !important; opacity: 0 !important; pointer-events: none !important; z-index: -9999 !important;
}
""")
print("✅ CSS do selo atualizado!")
