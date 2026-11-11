import re

with open('app/layout.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

error_script = """
    <script dangerouslySetInnerHTML={{ __html: `
      window.addEventListener('error', function(e) {
        var el = document.createElement('div');
        el.style = "position:fixed; top:0; left:0; width:100%; height:100%; background:white; color:red; z-index:99999; padding:20px; overflow:auto; font-family:monospace; font-size: 14px;";
        el.innerHTML = "<h1>ERRO NO NAVEGADOR:</h1><p>" + e.message + "</p><pre>" + (e.error ? e.error.stack : '') + "</pre>";
        document.body.appendChild(el);
      });
      window.addEventListener('unhandledrejection', function(e) {
        var el = document.createElement('div');
        el.style = "position:fixed; top:0; left:0; width:100%; height:100%; background:white; color:red; z-index:99999; padding:20px; overflow:auto; font-family:monospace; font-size: 14px;";
        el.innerHTML = "<h1>PROMISE REJECTION:</h1><p>" + e.reason + "</p>";
        document.body.appendChild(el);
      });
    `}} />
"""

if 'window.addEventListener(\'error\'' not in content:
    content = content.replace('<body>', '<body>' + error_script)
    with open('app/layout.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Script de captura de erro injetado no layout.tsx")
else:
    print("⚠️ Script já existe.")
