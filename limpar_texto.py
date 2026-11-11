import os

ignore_dirs = ['node_modules', '.git', '.next', '.netlify']
# Adicionando variações para garantir que pegue tudo
replacements = {
    'SINGITRONIC': 'ZIXLIMA',
    'Singitronic': 'Zixlima',
    'singitronic': 'zixlima',
    'ELECTRONIC ECOMMERCE': 'ELETRÔNICOS',
    'Electronic Ecommerce': 'Eletrônicos',
    'electronic ecommerce': 'eletrônicos',
    'Electronic Commerce': 'Eletrônicos'
}

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith(('.tsx', '.ts', '.js', '.jsx', '.html', '.json')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for old, new in replacements.items():
                content = content.replace(old, new)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Texto antigo removido de: {filepath}")

print("🎉 Varredura de texto concluída!")
