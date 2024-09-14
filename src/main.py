#"https://esaj.tjce.jus.br/cdje/index.do;jsessionid=F5863C3AC94BBA73B9F063A08841E9BF.cdje1"

from scraper.downloaderFunc import download_pdf
import os
import logging
import yaml

with open(r"C:\Users\liasa\OneDrive\Documentos\MeusProjetos\diario-da-justica\projeto-diario-da-justica\config\config.yaml", "r") as file:
    config = yaml.safe_load(file)

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(project_root, 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
# Verifica se o diretório foi criado corretamente
print(f"O diretório de logs está localizado em: {log_dir}")

log_file = os.path.join(log_dir, 'app.log')

logging.basicConfig(
    filename=log_file,
    level=config.get('log_level', logging.INFO),  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    logging.info('Início do script main.py')
    url_pdf = "https://esaj.tjce.jus.br/cdje/index.do;jsessionid=F5863C3AC94BBA73B9F063A08841E9BF.cdje1"
    path_download = r"C:\Users\liasa\Downloads"
    download_pdf(url_pdf, path_download)
    logging.info('Final do script main.py')
if __name__ == "__main__":
    main()
