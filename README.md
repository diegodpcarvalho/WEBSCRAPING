# 🕸️ Web Scraping - Download e Compactação de PDFs 🗂️

Este projeto foi desenvolvido como parte de um teste técnico para uma vaga de emprego. Ele demonstra o uso de **Web Scraping** com Python para acessar um site, localizar links de arquivos PDF específicos, baixá-los, e compactá-los em um único arquivo ZIP.

---

## 📋 Funcionalidades

1. **Acesso automático ao site da ANS**:
   - O script acessa a página: [Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos).

2. **Identificação e download de PDFs específicos**:
   - Apenas os anexos **"Anexo I"** e **"Anexo II"** são baixados, ignorando os demais arquivos presentes na página.

3. **Compactação dos arquivos**:
   - Após o download, todos os PDFs são compactados em um único arquivo ZIP.

4. **Controle de arquivos baixados**:
   - O script mantém um controle eficiente para evitar duplicatas e gerenciar os arquivos baixados.

---

## 💻 Tecnologias Utilizadas

- **Python 3.10**: Linguagem de programação utilizada no projeto.
- **Bibliotecas**:
  - `requests`: Para realizar requisições HTTP.
  - `BeautifulSoup (bs4)`: Para fazer o parsing do HTML e localizar os links dos PDFs.
  - `zipfile`: Para compactar os arquivos em um arquivo ZIP.
  - `os`: Para gerenciar arquivos no sistema operacional.

---

## 🚀 Como Executar o Projeto

1. **Clonar este repositório**:
   ```bash
   git clone https://github.com/diegodpcarvalho/WEBSCRAPING
   cd WEBSCRAPING

## Resultados:

Os arquivos "Anexo I" e "Anexo II" serão baixados e salvos no diretório do script.

Um arquivo chamado anexos.zip será gerado contendo os PDFs compactados.

## 📂 Estrutura do Código
main.py: O script principal que realiza todo o processo de scraping, download e compactação.

Dependências: Todas as bibliotecas necessárias estão listadas no arquivo requirements.txt.

## 📝 Explicação Técnica
1️⃣ Web Scraping com BeautifulSoup
O HTML da página é carregado e analisado para encontrar os links dos PDFs.

Foi utilizada a função soup.find_all para localizar <a> tags com os nomes exatos dos arquivos desejados ("Anexo I" e "Anexo II").

2️⃣ Download de PDFs
A biblioteca requests foi usada para fazer o download dos arquivos PDF.

Cada PDF foi salvo localmente com o nome original extraído do link.

3️⃣ Compactação dos Arquivos
Todos os PDFs baixados foram compactados em um único arquivo ZIP com a biblioteca zipfile.

4️⃣ Boas Práticas
O script foi projetado para ser robusto, verificando duplicatas e mantendo um controle eficiente dos arquivos baixados.

Links completos e relativos foram tratados de forma genérica, garantindo maior adaptabilidade do código.

## 🌟 Diferenciais
Filtro Inteligente:

Apenas os arquivos relevantes (Anexo I e Anexo II) são processados, economizando tempo e recursos.

Código Limpo e Bem Documentado:

O script foi escrito com clareza e inclui comentários explicativos para cada etapa.

Adaptabilidade:

O código é genérico o suficiente para ser adaptado a outras páginas que contenham arquivos semelhantes.

Controle de Erros:

Verificações foram adicionadas para lidar com links quebrados ou arquivos não encontrados.

👨‍💻 Autor
Desenvolvido por Diego de Paula Carvalho.

📧 diegodpcarvalho@gmail.com

🖥️ GitHub

