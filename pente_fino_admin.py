import os
import re

print("👑 INICIANDO VARREDURA SUPREMA DENTRO DO PAINEL ADMIN...\n")

# Dicionário focado 100% no Admin
traducoes_admin = {
    'Total Sales': 'Vendas Totais', 'Total Orders': 'Total de Pedidos',
    'Recent Orders': 'Pedidos Recentes', 'Customers': 'Clientes',
    'Customer Name': 'Nome do Cliente', 'Customer': 'Cliente',
    'Order': 'Pedido', 'Orders': 'Pedidos', 'Product': 'Produto', 'Products': 'Produtos',
    'Add Product': 'Adicionar Produto', 'Add User': 'Adicionar Usuário',
    'Add Category': 'Adicionar Categoria', 'Edit Product': 'Editar Produto',
    'Edit User': 'Editar Usuário', 'Edit Category': 'Editar Categoria',
    'Update Product': 'Atualizar Produto', 'Delete': 'Excluir', 'Edit': 'Editar',
    'Save': 'Salvar', 'Save Changes': 'Salvar Alterações', 'Cancel': 'Cancelar',
    'Search': 'Pesquisar', 'Search by name': 'Buscar por nome',
    'Status': 'Status', 'Pending': 'Pendente', 'Completed': 'Concluído',
    'Cancelled': 'Cancelado', 'Delivered': 'Entregue', 'Shipped': 'Enviado',
    'Price': 'Preço', 'Quantity': 'Quantidade', 'Total': 'Total',
    'Date': 'Data', 'Actions': 'Ações', 'Name': 'Nome', 'Email': 'E-mail',
    'Password': 'Senha', 'Role': 'Função', 'Admin': 'Administrador', 'User': 'Usuário',
    'Image': 'Imagem', 'Upload Image': 'Enviar Imagem', 'Bulk Upload': 'Upload em Massa',
    'Settings': 'Configurações', 'Dashboard': 'Painel de Controle'
}

target_pastas = ['app/(dashboard)/admin', 'components/DashboardSidebar.tsx', 'components/DashboardProductTable.tsx']
total_ajustes = 0

for target in target_pastas:
    if not os.path.exists(target): continue
    
    # Se for pasta, varre tudo dentro. Se for arquivo, varre só ele.
    paths_to_walk = []
    if os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(('.tsx', '.jsx')): paths_to_walk.append(os.path.join(root, file))
    else:
        paths_to_walk.append(target)

    for filepath in paths_to_walk:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # 1. Tradução de textos (apenas entre tags e placeholders)
        for eng, pt in traducoes_admin.items():
            content = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', content, flags=re.IGNORECASE)
            content = re.sub(r'placeholder=["\']' + re.escape(eng) + r'["\']', f'placeholder="{pt}"', content, flags=re.IGNORECASE)
            content = re.sub(r'title=["\']' + re.escape(eng) + r'["\']', f'title="{pt}"', content, flags=re.IGNORECASE)

        # 2. Conserto de Tabelas (Responsividade no celular)
        # Envolve tabelas em uma div com overflow-x-auto para não quebrar a tela
        if '<table' in content and 'overflow-x-auto' not in content:
            # Uma tática simples: substituir a div que envolve a tabela
            content = content.replace('<table', '<div className="overflow-x-auto w-full"><table')
            content = content.replace('</table>', '</table></div>')
            print(f"📱 Tabela ajustada para mobile em: {filepath}")

        # 3. Conserto de Larguras Fixas (evita estourar a tela)
        content = re.sub(r'w-\[(\d{3,})px\]', 'w-full max-w-full', content)
        content = re.sub(r'width=["\'](\d{3,})["\']', 'width="100%"', content)

        # 4. Correção de Margens Exageradas (que empurram o conteúdo para fora)
        content = content.replace('ml-64', 'md:ml-64 ml-0') # Ajusta a barra lateral no celular

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            total_ajustes += 1
            print(f"✅ Admin ajustado: {filepath}")

print(f"\n🎉 Pente fino no Admin concluído! {total_ajustes} arquivos ajustados para tradução e responsividade.")
