import os
import re

# Dicionário Ultra Full
traducoes = {
    # Marca antiga
    'Singitronic': 'Zixlima Eletrônicos', 'SINGITRONIC': 'ZIXLIMA ELETRÔNICOS',
    'Electronic Ecommerce': 'Eletrônicos', 'ELECTRONIC ECOMMERCE': 'ELETRÔNICOS',
    
    # E-commerce e Produtos
    'Add to cart': 'Adicionar ao Carrinho', 'Add to Cart': 'Adicionar ao Carrinho',
    'Buy Now': 'Comprar Agora', 'Buy now': 'Comprar Agora',
    'Out of stock': 'Esgotado', 'In stock': 'Em Estoque',
    'Price': 'Preço', 'Total': 'Total', 'Subtotal': 'Subtotal',
    'Category': 'Categoria', 'Categories': 'Categorias',
    'Product': 'Produto', 'Products': 'Produtos',
    'Reviews': 'Avaliações', 'Description': 'Descrição',
    'Quantity': 'Quantidade', 'Checkout': 'Finalizar Compra',
    'Continue shopping': 'Continuar Comprando', 'Empty cart': 'Carrinho Vazio',
    'Search': 'Pesquisar', 'Search Results': 'Resultados da Busca',
    
    # Navegação e Botões
    'Home': 'Início', 'Shop': 'Loja', 'Login': 'Entrar', 'Register': 'Cadastrar',
    'Logout': 'Sair', 'Submit': 'Enviar', 'Cancel': 'Cancelar', 'Save': 'Salvar',
    'Delete': 'Excluir', 'Edit': 'Editar', 'Update': 'Atualizar', 'Back': 'Voltar',
    'Next': 'Próximo', 'Previous': 'Anterior', 'Loading': 'Carregando',
    'Are you sure?': 'Tem certeza?', 'Yes': 'Sim', 'No': 'Não',
    'Sort by': 'Ordenar por', 'Filter': 'Filtrar', 'Filters': 'Filtros',
    'Clear all': 'Limpar tudo', 'Showing': 'Mostrando', 'Results': 'Resultados'
}

pastas = ['app', 'components', 'lib', 'utils', 'src']
total_ajustes = 0

print("🔍 Iniciando Varredura Ultra Site Total Full...\n")

for pasta in pastas:
    if not os.path.exists(pasta): continue
    for root, dirs, files in os.walk(pasta):
        if 'node_modules' in root or '.next' in root or '.git' in root: continue
        for file in files:
            if file.endswith(('.tsx', '.ts', '.js', '.jsx')):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original = content
                
                # 1. Substituição da marca antiga (segura, em qualquer lugar)
                for brand in ['Singitronic', 'SINGITRONIC', 'Electronic Ecommerce', 'ELECTRONIC ECOMMERCE']:
                    if brand in content:
                        content = content.replace(brand, 'Zixlima Eletrônicos' if brand[0].isupper() else 'ZIXLIMA ELETRÔNICOS')

                # 2. Tradução segura (apenas UI)
                for eng, pt in traducoes.items():
                    # Texto entre tags HTML
                    content = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', content, flags=re.IGNORECASE)
                    # Placeholders
                    content = re.sub(r'placeholder=["\']' + re.escape(eng) + r'["\']', f'placeholder="{pt}"', content, flags=re.IGNORECASE)
                    # Títulos (tooltips)
                    content = re.sub(r'title=["\']' + re.escape(eng) + r'["\']', f'title="{pt}"', content, flags=re.IGNORECASE)
                    # Alt de imagens
                    content = re.sub(r'alt=["\']' + re.escape(eng) + r'["\']', f'alt="{pt}"', content, flags=re.IGNORECASE)
                    # Alertas simples (alert("Texto"))
                    content = re.sub(r'alert\(["\']' + re.escape(eng) + r'["\']\)', f'alert("{pt}")', content, flags=re.IGNORECASE)

                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Ajustado: {filepath}")
                    total_ajustes += 1

print(f"\n🎉 Varredura Ultra Full concluída! {total_ajustes} arquivos ajustados.")
