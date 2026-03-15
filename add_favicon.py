import os
import re

def add_favicon(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Verifica se já tem alguma tag de favicon
    if 'favicon' in content.lower() or 'icon' in content.lower():
        print(f"Arquivo {html_file} já contém tags de favicon. Pulando...")
        return
    
    # Adiciona as tags de favicon após a tag <title>
    favicon_tags = '''
    <!-- Favicon em múltiplos formatos para melhor compatibilidade -->
    <link rel="icon" type="image/x-icon" href="icone_chordflow.ico">
    <link rel="shortcut icon" type="image/x-icon" href="icone_chordflow.ico">
    <link rel="icon" type="image/png" sizes="16x16" href="icone_chordflow-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="icone_chordflow-32x32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="icone_chordflow-180x180.png">
    <meta name="msapplication-TileImage" content="icone_chordflow-144x144.png">
    '''
    
    # Encontra a posição após a tag </title>
    title_end = content.find('</title>')
    if title_end == -1:
        print(f"Aviso: Não foi encontrada a tag </title> em {html_file}")
        return
    
    # Insere as tags de favicon após o </title>
    new_content = content[:title_end + 8] + favicon_tags + content[title_end + 8:]
    
    # Salva o arquivo
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"Favicon adicionado com sucesso em {html_file}")

# Lista de arquivos HTML no diretório atual
html_files = [f for f in os.listdir() if f.endswith('.html')]

# Adiciona favicon em todos os arquivos HTML
for html_file in html_files:
    add_favicon(html_file)
