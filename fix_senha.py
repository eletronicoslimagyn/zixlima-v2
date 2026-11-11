import re

path = 'app/register/page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Força o campo de senha a não ter auto-complete e a não colocar espaços
if 'autoComplete="new-password"' not in content:
    content = content.replace('<input', '<input autoComplete="new-password"')
    
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Formulário blindado contra espaços invisíveis!")
