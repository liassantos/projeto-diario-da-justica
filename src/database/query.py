import os
import logging
import mysql.connector
from dotenv import load_dotenv

def pesquisar_processo(numeros_processos):
    
    load_dotenv()

    logger = logging.getLogger(__name__)

    try:

        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),   
            user=os.getenv('DB_USER'), 
            password=os.getenv('DB_PASSWORD'), 
            database=os.getenv('DB_DATABASE')
        )
        logger.info("Conexão co banco de dados estabelecida.")
        try:
            cursor = conn.cursor()
            logger.info("Cursor criado.")

            try:
                if isinstance(numeros_processos, list):
                    placeholders = ', '.join(['%s'] * len(numeros_processos))
                    sql = f"SELECT * FROM dados WHERE processo IN ({placeholders})"
                    cursor.execute(sql, numeros_processos)
                else:
                    cursor.execute("SELECT * FROM dados WHERE processo = %s", (numeros_processos,))
            
                result = cursor.fetchall()
                logger.info("Query realizada com sucesso.")

            except Exception as e:
                logger.error(f"Query não realizada: {e}")

        except Exception as e:
            logger.error(f"Não foi possível criar o cursor: {e}")
    
    except Exception as e:
        logger.error(f"Não foi possível estabelecer conexão com banco de dados: {e}")
        

    finally:
        try:
            conn.close()
            logger.info("Conexão com banco de dados fechada.")
            return result
        
        except Exception as e:
            logger.error(f"Não foi possível finalizar operação: {e}")

