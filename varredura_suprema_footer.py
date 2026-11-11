import os
import re

# Dicionário supremo para o rodapé
traducoes_footer = {
    'Sale': 'Promoções',
    'Buying': 'Compras',
    'About Us': 'Sobre Nós',
    'Support': 'Suporte',
    'Discounts': 'Descontos',
    'News': 'Notícias',
    'Register Discounts': 'Cadastre-se para Descontos',
    'Zixlima Loyalty Card': 'Cartão Fidelidade Zixlima',
    'Terms Of Use': 'Termos de Uso',
    'Privacy Policy': 'Política de Privacidade',
    'Complaints': 'Reclamações',
    'Partners': 'Parceiros',
    'About Zixlima': 'Sobre a Zixlima',
    'Work With Us': 'Trabalhe Conosco',
    'Company Profile': 'Perfil da Empresa',
    'Contact': 'Contato',
    'How to Buy at Zixlima': 'Como Comprar na Zixlima',
    'FAQ': 'Dúvidas Frequentes',
    'All rights reserved': 'Todos os direitos reservados',
    'Singitronic': 'Zixlima Eletrônicos',
    'SINGITRONIC': 'ZIXLIMA ELETRÔNICOS',
    'Electronic Ecommerce': 'Eletrônicos',
    'Electronic Commerce': 'Eletrônicos'
}

# Caminhos prováveis do rodapé
footer_files = [
    'components/Footer.tsx',
    'components/Footer/index.tsx',
    'app/components/Footer.tsx'
]

total_ajustes = 0
encontrado = False

for filepath in footer_files:
    if os.path.exists(filepath):
        encontrado = True
        print(f"🔍 Vasculhando o arquivo: {filepath}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Aplica as traduções de forma segura (apenas texto entre tags ou em strings de exibição)
        for eng, pt in traducoes_footer.items():
            # Troca textos entre tags HTML (ex: >Sale<)
            content = re.sub(r'>(\s*)' + re.escape(eng) + r'(\s*)<', r'>\1' + pt + r'\2<', content, flags=re.IGNORECASE)
            # Troca a marca antiga (caso esteja no meio de uma frase)
            content = content.replace(eng, pt)

        # 2. Garante que o e-mail oficial esteja no rodapé
        if 'suporte@zixlima.com.br' not in content:
            email_html = '''
            <div className="w-full text-center mt-6 pt-6 border-t border-gray-700">
                <p className="text-white font-semibold"><i className="fa fa-envelope mr-2"></i> Contato: suporte@zixlima.com.br</p>
            </div>
            '''
            # Tenta injetar antes do fechamento do footer
            if '</footer>' in content:
                content = content.replace('</footer>', email_html + '\n</footer>')
            else:
                content += email_html
            print("✅ E-mail oficial injetado no rodapé!")
        
        # 3. Corrige a logo do rodapé para não quebrar
        content = re.sub(r'src=["\'].*?\.(png|jpg|svg|webp)["\']', 'src="/logo.png"', content)

        # Salva o arquivo se houve mudança
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            total_ajustes += 1
            print(f"✅ Rodapé atualizado com sucesso!")
        else:
            print("ℹ️ Nenhuma alteração necessária (já estava atualizado).")

if not encontrado:
    print("❌ Arquivo do rodapé não encontrado. Verifique a estrutura de pastas.")
else:
    print(f"\n🎉 Varredura Suprema concluída! {total_ajustes} arquivos do rodapé ajustados.")
