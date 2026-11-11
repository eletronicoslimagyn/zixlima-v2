import os
import re

pastas = ['app', 'components', 'src']
old_brand = ['Singitronic', 'SINGITRONIC', 'singitronic', 'Electronic Ecommerce', 'ELECTRONIC ECOMMERCE', 'Electronic Commerce']

traducoes = {
    'Login': 'Entrar', 'Register': 'Cadastrar', 'Logout': 'Sair',
    'Home': 'Início', 'Shop': 'Loja', 'Search': 'Pesquisar',
    'Cart': 'Carrinho', 'Checkout': 'Finalizar Compra',
    'Price': 'Preço', 'Total': 'Total', 'Subtotal': 'Subtotal',
    'Shipping': 'Frete', 'Quantity': 'Quantidade',
    'Add to cart': 'Adicionar ao Carrinho', 'Buy now': 'Comprar Agora',
    'Filters': 'Filtros', 'Availability': 'Disponibilidade',
    'In stock': 'Em estoque', 'Out of stock': 'Esgotado',
    'Default': 'Padrão', 'Page': 'Página',
    'Categories': 'Categorias', 'Products': 'Produtos',
    'Orders': 'Pedidos', 'Users': 'Usuários', 'Settings': 'Configurações',
    'Dashboard': 'Painel', 'Sort A-Z': 'Ordenar A-Z', 'Sort Z-A': 'Ordenar Z-A',
    'Lowest Price': 'Menor Preço', 'Highest Price': 'Maior Preço',
    'Min Price': 'Preço Mínimo', 'Max Price': 'Preço Máximo'
}

print("🔍 Iniciando varredura inteligente...\n")
total_ajustes = 0

for pasta in pastas:
    if not os.path.exists(pasta): continue
    for root, dirs, files in os.walk(pasta):
        if 'node_modules' in root or '.next' in root: continue
        for file in files:
            if file.endswith(('.tsx', '.ts', '.js', '.jsx')):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                modificado = False
                for i, line in enumerate(lines):
                    original = line

                    # 1. Caça a marca antiga (em qualquer lugar do texto)
                    for brand in old_brand:
                        if brand in line:
                            line = line.replace(brand, 'Zixlima Eletrônicos')
                            print(f"🏢 Marca trocada em {filepath} (linha {i+1})")
                    
                    # 2. Traduz APENAS textos entre tags HTML ou em placeholders
                    for eng, pt in traducoes.items():
                        # Regex para >Texto<
                        line = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', line, flags=re.IGNORECASE)
                        # Regex para placeholder="Texto"
                        line = re.sub(r'placeholder=["\']' + re.escape(eng) + r'["\']', f'placeholder="{pt}"', line, flags=re.IGNORECASE)
                        # Regex para title="Texto"
                        line = re.sub(r'title=["\']' + re.escape(eng) + r'["\']', f'title="{pt}"', line, flags=re.IGNORECASE)

                    if line != original:
                        lines[i] = line
                        modificado = True
                        total_ajustes += 1
                        print(f"🌐 Traduzido em {filepath} (linha {i+1}): {original.strip()[:50]}...")

                if modificado:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(lines)

print(f"\n🎉 Varredura concluída! {total_ajustes} ajustes seguros realizados.")
