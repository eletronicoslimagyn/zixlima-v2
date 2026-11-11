import os
import re

def adicionar_olho(filepath, is_register=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Garantir "use client" e imports
    if '"use client"' not in content and "'use client'" not in content:
        content = '"use client";\n' + content
    
    if 'useState' not in content:
        content = 'import { useState } from "react";\n' + content
        
    if 'FaEye' not in content:
        content = 'import { FaEye, FaEyeSlash } from "react-icons/fa";\n' + content

    # 2. Adicionar estados (se não existirem)
    match = re.search(r'(export default function \w+\([^)]*\)\s*\{)', content)
    if match and 'showPassword' not in content:
        state_code = '\n  const [showPassword, setShowPassword] = useState(false);\n'
        if is_register:
            state_code += '  const [showConfirmPassword, setShowConfirmPassword] = useState(false);\n'
        content = content[:match.end()] + state_code + content[match.end():]

    # 3. Substituir o primeiro input de senha
    def replace_password(match):
        attrs_before = match.group(1)
        attrs_after = match.group(2)
        return f'''<div className="relative w-full">
            <input{attrs_before}type={{showPassword ? "text" : "password"}}{attrs_after}>
            <button type="button" onClick={{() => setShowPassword(!showPassword)}} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-700">
                {{showPassword ? <FaEyeSlash /> : <FaEye />}}
            </button>
        </div>'''

    content = re.sub(r'<input([^>]*)type="password"([^>]*)>', replace_password, content, count=1)

    # 4. Se for o cadastro, substituir o segundo input (Confirme a senha)
    if is_register and 'showConfirmPassword' in content:
        def replace_confirm_password(match):
            attrs_before = match.group(1)
            attrs_after = match.group(2)
            return f'''<div className="relative w-full">
                <input{attrs_before}type={{showConfirmPassword ? "text" : "password"}}{attrs_after}>
                <button type="button" onClick={{() => setShowConfirmPassword(!showConfirmPassword)}} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-700">
                    {{showConfirmPassword ? <FaEyeSlash /> : <FaEye />}}
                </button>
            </div>'''
        
        content = re.sub(r'<input([^>]*)type="password"([^>]*)>', replace_confirm_password, content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Olhinho adicionado em: {filepath}")

# Executar
adicionar_olho('app/login/page.tsx', is_register=False)
adicionar_olho('app/register/page.tsx', is_register=True)
