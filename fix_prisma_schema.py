import re

with open('prisma/schema.prisma', 'r', encoding='utf-8') as f:
    content = f.read()

# Procura o bloco do generator e substitui por um limpo e sem o "previewFeatures" (que está deprecado)
pattern = r'generator client\s*\{[^}]*\}'
new_generator = """generator client {
  provider      = "prisma-client-js"
  binaryTargets = ["native", "rhel-openssl-1.0.x", "rhel-openssl-3.0.x"]
}"""

content = re.sub(pattern, new_generator, content)

with open('prisma/schema.prisma', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Schema do Prisma limpo e corrigido!")
