import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# 1. Acesso ao site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)

# 2. Scraping do conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Encontrando os links dos arquivos PDF (Anexo I e II)
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    # Procurar especificamente pelos Anexos I e II e garantir que seja um arquivo PDF
    if ('Anexo_I' in href or 'Anexo_II' in href) and href.endswith('.pdf'):
        pdf_links.append(href)

# 4. Download dos arquivos PDF
downloaded_files = []
for pdf_link in pdf_links:
    pdf_url = pdf_link if pdf_link.startswith('http') else f"https://www.gov.br{pdf_link}"
    pdf_name = pdf_url.split('/')[-1]

    # Garantir que o nome do arquivo seja único
    count = 1
    original_pdf_name = pdf_name
    while pdf_name in downloaded_files:
        pdf_name = f"{original_pdf_name.split('.')[0]}_{count}.pdf"
        count += 1

    # Realizando o download do arquivo
    response = requests.get(pdf_url)
    with open(pdf_name, 'wb') as file:
        file.write(response.content)
        downloaded_files.append(pdf_name)
        print(f"Baixado: {pdf_name}")

# 5. Compactação em arquivo ZIP
zip_filename = "anexos.zip"
with ZipFile(zip_filename, 'w') as zipf:
    for file in downloaded_files:
        zipf.write(file, os.path.basename(file))  # Adiciona o arquivo ao ZIP

# 6. Remover os arquivos PDF baixados após compactar
for file in downloaded_files:
    try:
        os.remove(file)
        print(f"Removido: {file}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file}")

print(f"Todos os anexos foram compactados em: {zip_filename}")
