import os

for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.next' in root:
        continue
    for file in files:
        if file.endswith(('.tsx', '.ts', '.js', '.jsx')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Corrige as variações quebradas do banner
            content = content.replace('APRESENTANDO O SINGITRONIC', 'APRESENTANDO A ZIXLIMA')
            content = content.replace('SINGI TRONIC', 'ZIXLIMA ELETRÔNICOS')
            content = content.replace('SINGITRONIC', 'ZIXLIMA ELETRÔNICOS')
            content = content.replace('Singitronic', 'Zixlima Eletrônicos')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
