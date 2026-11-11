import re

path = 'app/layout.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'WhatsAppButton' not in content:
    content = 'import WhatsAppButton from "./WhatsAppButton";\n' + content

if '<WhatsAppButton />' not in content:
    # Coloca o botão bem no final do body
    content = content.replace('</body>', '  <WhatsAppButton />\n</body>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Botão do WhatsApp injetado com sucesso!")
