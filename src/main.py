import os
import logging
import yaml
from scraper.downloader import download_pdf
from scraper.pdf_reader import extrair_texto
from database.query import pesquisar_processo
from mail.gmail import enviar_email
from dotenv import load_dotenv



def main():
    load_dotenv()

    with open(os.getenv(r"PATH_YALM"), "r") as file:
        config = yaml.safe_load(file)

    logger = logging.getLogger(os.path.basename(__file__))

    file_handler = logging.FileHandler(os.getenv(r"PATH_LOG"), 'a')
    file_handler.setLevel(logging.WARNING)

    stream_handler = logging.StreamHandler()

    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(asctime)s - %(name)s - %(message)s',
        handlers=[stream_handler, file_handler]
        )
    
    logger.info('Início do script main.py')

    url = os.getenv("DOWNLOAD_URL")

    path_download = os.getenv(r"PATH_DOWNLOAD")

    caminho_pdf = os.getenv(r"PATH_PDF")

    download_pdf(url, path_download)

    lista_processos = extrair_texto(caminho_pdf)

    resultado_query = pesquisar_processo(lista_processos)
    
    logger.info(f"O resultado da pesquisa no banco de dados foi: {resultado_query}")

    enviar_email(resultado_query)

    logger.info('Final do script main.py')


if __name__ == "__main__":
    main()
