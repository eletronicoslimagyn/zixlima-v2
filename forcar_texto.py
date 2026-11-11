import os

ignore_dirs = ['node_modules', '.git', '.next', '.netlify']
replacements = {
    'SINGITRONIC': 'ZIXLIMA',
    'Singitronic': 'Zixlima',
    'singitronic': 'zixlima',
    'ELECTRONIC ECOMMERCE': 'ELETRÔNICOS',
    'Electronic Ecommerce': 'Eletrônicos'
}

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        # Incluindo .css e .svg na busca
        if file.endswith(('.tsx', '.ts', '.js', '.jsx', '.html', '.json', '.css', '.svg')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for old, new in replacements.items():
                content = content.replace(old, new)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Texto trocado em: {filepath}")

print("🎉 Varredura profunda concluída!")
