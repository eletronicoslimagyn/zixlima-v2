import re

path = 'app/layout.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Adiciona o import se não existir
if 'ErrorReporter' not in content:
    content = 'import ErrorReporter from "./ErrorReporter";\n' + content

# Adiciona o componente antes do fechamento da tag </body>
if '<ErrorReporter />' not in content:
    content = content.replace('</body>', '  <ErrorReporter />\n</body>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Layout atualizado com o ErrorReporter!")
