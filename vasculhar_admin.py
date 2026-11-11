import os
import re

# Lista de termos comuns no painel de admin em inglês
traducoes = {
    'Dashboard': 'Painel',
    'Orders': 'Pedidos',
    'Products': 'Produtos',
    'Categories': 'Categorias',
    'Users': 'Usuários',
    'Settings': 'Configurações',
    'Add New': 'Adicionar Novo',
    'Add new': 'Adicionar novo',
    'Add Product': 'Adicionar Produto',
    'Add Category': 'Adicionar Categoria',
    'Add User': 'Adicionar Usuário',
    'Edit': 'Editar',
    'Delete': 'Excluir',
    'Save': 'Salvar',
    'Cancel': 'Cancelar',
    'Update': 'Atualizar',
    'Status': 'Status',
    'Date': 'Data',
    'Customer': 'Cliente',
    'Price': 'Preço',
    'Quantity': 'Quantidade',
    'Image': 'Imagem',
    'Name': 'Nome',
    'Description': 'Descrição',
    'Category': 'Categoria',
    'Submit': 'Enviar',
    'Back': 'Voltar',
    'Actions': 'Ações',
    'All': 'Todos',
    'Search': 'Pesquisar',
    'Bulk Upload': 'Upload em Massa',
    'Merchant': 'Lojista',
    'Total': 'Total',
    'Order ID': 'ID do Pedido',
    'Product Name': 'Nome do Produto',
    'Price (R$)': 'Preço (R$)',
    'Stock': 'Estoque',
    'In Stock': 'Em Estoque',
    'Out of Stock': 'Esgotado'
}

# Pastas e arquivos alvo
targets = [
    'app/(dashboard)/admin',
    'components/DashboardSidebar.tsx'
]

total_ajustes = 0

for target in targets:
    if not os.path.exists(target):
        continue
        
    # Se for um diretório, varre os arquivos dentro
    if os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(('.tsx', '.ts', '.js', '.jsx')):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    modificado = False
                    for i, line in enumerate(lines):
                        original = line
                        for eng, pt in traducoes.items():
                            # Regex restrita para não quebrar variáveis (só troca entre tags HTML ou em props visuais)
                            line = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', line, flags=re.IGNORECASE)
                            line = re.sub(r'placeholder=["\']' + re.escape(eng) + r'["\']', f'placeholder="{pt}"', line, flags=re.IGNORECASE)
                            line = re.sub(r'title=["\']' + re.escape(eng) + r'["\']', f'title="{pt}"', line, flags=re.IGNORECASE)
                            line = re.sub(r'label=["\']' + re.escape(eng) + r'["\']', f'label="{pt}"', line, flags=re.IGNORECASE)
                            
                        if line != original:
                            lines[i] = line
                            modificado = True
                            total_ajustes += 1
                            print(f"🌐 Traduzido em {filepath}: {original.strip()[:40]}...")
                    
                    if modificado:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                            
    # Se for um arquivo específico
    elif os.path.isfile(target):
        with open(target, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for eng, pt in traducoes.items():
            content = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', content, flags=re.IGNORECASE)
        
        if content != original:
            with open(target, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"🌐 Traduzido no componente: {target}")
            total_ajustes += 1

print(f"\n🎉 Varredura do Admin concluída! {total_ajustes} ajustes realizados.")
