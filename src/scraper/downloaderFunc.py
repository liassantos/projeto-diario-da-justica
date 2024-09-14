from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def download_pdf(url, downloadPath):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    prefs = {"download.default_directory": downloadPath,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enabled": True}
    chrome_options.add_experimental_option("prefs", prefs) 

    try:
        service = Service(executable_path=r"C:\Users\liasa\OneDrive\Documentos\MeusProjetos\diario-da-justica\projeto-diario-da-justica\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logger.info("Driver do Chrome inicializado com sucesso")

        try:
            logger.info("Navegando para o Diário")
            driver.get(url)
            logger.info(f"Título da página: {driver.title}")
            logger.info(f"URL atual: {driver.current_url}")

            try:
                logger.info("Tentando selecionar o caderno 2 - judiciário")
                caderno_select = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "cadernosCad"))
                )
                caderno_select.send_keys("caderno 2 - Judiciario")
                logger.info("Caderno selecionado com sucesso")

            except Exception as e:
                logger.error(f"Erro ao selecionar o caderno: {e}")

            try:
                logger.info("Tentando clicar no botão de download")
                download_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "download"))
                )
                download_button.click()
                logger.info("Botão de download clicado com sucesso")

                # Aguardar um tempo para o download iniciar
                time.sleep(10)
                logger.info("Aguardado 10 segundos após o clique no download")

            except Exception as e:
                logger.error(f"Erro ao clicar no botão de download: {e}")

        except Exception as e:
            logger.error(f"Erro durante a navegação ou interação com a página: {e}")

    except Exception as e:
        logger.error(f"Erro ao inicializar o driver do Chrome: {e}")

    finally:
        logger.info("Tentando fechar o navegador")
        try:
            driver.quit()
            logger.info("Navegador fechado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao fechar o navegador: {e}")
            