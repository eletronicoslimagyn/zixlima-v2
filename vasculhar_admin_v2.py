import os
import re

# Dicionário expandido com termos de formulários e tabelas de Admin
traducoes = {
    'Product Name': 'Nome do Produto', 'Price': 'Preço', 'Description': 'Descrição',
    'Category': 'Categoria', 'Stock': 'Estoque', 'Image': 'Imagem',
    'Upload': 'Carregar', 'Choose File': 'Escolher Arquivo', 'Submit': 'Enviar',
    'Save Changes': 'Salvar Alterações', 'Save': 'Salvar', 'Cancel': 'Cancelar',
    'Delete': 'Excluir', 'Edit': 'Editar', 'Update': 'Atualizar',
    'Product Details': 'Detalhes do Produto', 'Add New Product': 'Adicionar Novo Produto',
    'Add New Category': 'Adicionar Nova Categoria', 'Add New User': 'Adicionar Novo Usuário',
    'Order ID': 'ID do Pedido', 'Customer': 'Cliente', 'Status': 'Status',
    'Date': 'Data', 'Total': 'Total', 'Actions': 'Ações', 'Name': 'Nome',
    'Email': 'E-mail', 'Password': 'Senha', 'Role': 'Função', 'Admin': 'Administrador',
    'User': 'Usuário', 'Quantity': 'Quantidade', 'In Stock': 'Em Estoque',
    'Out of Stock': 'Esgotado', 'Featured': 'Destaque', 'Yes': 'Sim', 'No': 'Não',
    'Confirm': 'Confirmar', 'Are you sure?': 'Tem certeza?', 'Loading': 'Carregando'
}

target = 'app/(dashboard)/admin'
total_ajustes = 0

if not os.path.exists(target):
    print("Pasta do admin não encontrada.")
else:
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
                        # Traduz o texto entre tags HTML (>Texto<)
                        line = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', line, flags=re.IGNORECASE)
                        # Traduz placeholders (placeholder="Texto")
                        line = re.sub(r'placeholder=["\']' + re.escape(eng) + r'["\']', f'placeholder="{pt}"', line, flags=re.IGNORECASE)
                        # Traduz labels de componentes (label="Texto")
                        line = re.sub(r'label=["\']' + re.escape(eng) + r'["\']', f'label="{pt}"', line, flags=re.IGNORECASE)
                        # Traduz títulos de botões/links (title="Texto")
                        line = re.sub(r'title=["\']' + re.escape(eng) + r'["\']', f'title="{pt}"', line, flags=re.IGNORECASE)
                        # Traduz aria-labels
                        line = re.sub(r'aria-label=["\']' + re.escape(eng) + r'["\']', f'aria-label="{pt}"', line, flags=re.IGNORECASE)

                    if line != original:
                        lines[i] = line
                        modificado = True
                        total_ajustes += 1
                        print(f"🌐 Traduzido em {filepath}: {original.strip()[:40]}...")

                if modificado:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(lines)

print(f"\n🎉 Varredura profunda do Admin concluída! {total_ajustes} ajustes realizados.")
