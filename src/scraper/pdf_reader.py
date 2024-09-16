import re
import pymupdf
import logging


def extrair_texto(caminho):
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Abrindo o documento")
        doc = pymupdf.Document(caminho)
        
        try:
            texto = ""
            logger.info("Extraindo texto do pdf")
            for pagina in doc:
                texto += pagina.get_text("textpage")
            logger.info("Fechando o documento")
            doc.close()
            
            try:
                logger.info("Encontrando os números de processo do pdf")
                lista = re.findall(r'[0-9]{7}-[0-9]{2}\.[0-9]{4}\.[0-9]\.[0-9]{2}\.[0-9]{4}', texto)
                logger.info("Números de processo encontrados. Salvos em uma lista.")
                return lista
            
            except Exception as e:
                logger.error(f"Números de processo não encontrados, devido ao erro: {e}")
        
        except Exception as e:
            logger.error(f"Não foi possível extrair o texto, devido ao erro: {e}")
    
    except Exception as e:
        logger.error(f"Não foi possível abrir o documento, devido ao erro: {e}")
    
    finally:
        logger.info("Saindo da função.")

