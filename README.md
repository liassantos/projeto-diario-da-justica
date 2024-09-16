
# Automação de Monitoramento de Processos Judiciais

Este projeto é uma automação em Python que acessa o site do Tribunal de Justiça do Ceará, faz o download do Diário da Justiça, processa os arquivos PDF para identificar atualizações em processos judiciais e envia um email com um relatório dos processos que foram atualizados no banco de dados local (MySQL).

## Funcionalidades

- Acessa o site do Tribunal de Justiça do Ceará.
- Faz o download do Diário da Justiça.
- Extrai e compara os processos encontrados no PDF com um banco de dados MySQL local.
- Envia um relatório por email para um destinatário definido com todos os processos presentes no banco de dados que foram atualizados.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```bash
projeto_automacao/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── downloader.py
│   │   ├── pdf_reader.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── query.py
│   ├── email/
│   │   ├── __init__.py
│   │   ├── gmail.py
├── config/
│   ├── config.yaml
├── logs/
├── requirements.txt
├── README.md
└── setup.py
```

- **`src/scraper/`**: Contém scripts responsáveis por baixar o PDF e ler o conteúdo dos arquivos do Diário da Justiça.
- **`src/database/`**: Inclui scripts para conexão com o banco de dados MySQL e consultas aos dados dos processos.
- **`src/email/`**: Script responsável por enviar o relatório de processos atualizados por email.
- **`config/config.yaml`**: Contém configurações do projeto, como credenciais do banco de dados, destinatários do email e URLs.
- **`logs/`**: Diretório para armazenar logs de execução.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **MySQL**: Banco de dados usado para armazenar os processos.
- **Selenium**: Automação do navegador para acessar e fazer download do Diário da Justiça.
- **PyMuPDF**: Biblioteca para ler e processar PDFs.
- **Python-dotenv**: Carrega variáveis de ambiente a partir de um arquivo `.env`.
- **SMTP**: Protocolo para envio de emails com o relatório.

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado as dependências necessárias. Você pode encontrá-las no arquivo `requirements.txt`.

### Instalação das Dependências

Execute o comando abaixo para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

## Execução

1. Configure suas credenciais e parâmetros no arquivo `config/config.yaml`.
2. Execute o script principal:

```bash
python src/main.py
```

O sistema fará o download do Diário da Justiça, verificará os processos no banco de dados e enviará um relatório por email.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

