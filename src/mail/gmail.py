import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, timedelta
from dotenv import load_dotenv


def pegar_data():
    
    data_dj = date.today() - timedelta(days=1)

    if data_dj.weekday() >= 5:
        dias_para_sexta = data_dj.weekday() - 4
        data_dj = data_dj - timedelta(days=dias_para_sexta)
    else:
        pass
    return data_dj.strftime(r"%d/%m/%Y")


def enviar_email(resultado_query):

    load_dotenv()

    logger = logging.getLogger(__name__)

    data = pegar_data()

    if resultado_query != []:
        quantidade_atualizacoes = len(resultado_query)

        linhas_tabela = ""

        for tupla in resultado_query:
            linhas_tabela += f'''<tr>
                        <th scope="row">{tupla[1]}</th>
                        <td>{tupla[2]}</td>
                        <td>{tupla[3]}</td>
                        <td>{tupla[4]}</td>
                        <td>{tupla[5]}</td>
                        <td>{tupla[6]}</td>
                    </tr>'''


        corpo = f'''<html>
        <head>
            <style>
                table {{
                    border-collapse: collapse;
                    border: 2px solid rgb(140, 140, 140);
                    font-family: sans-serif;
                    font-size: 0.8rem;
                    letter-spacing: 1px;
                }}
                
                thead, tfoot {{
                    background-color: rgb(228, 240, 245);
                }}
                
                th, td {{
                    border: 1px solid rgb(160, 160, 160);
                    padding: 8px 10px;
                }}
                
                td:last-of-type {{
                    text-align: center;
                }}
                
                tbody > tr:nth-of-type(even) {{
                    background-color: rgb(237, 238, 242);
                }}
                
                tfoot th {{
                    text-align: right;
                }}
                
                tfoot td {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <p><b>Bom dia, Usuário! Tudo bom?</b></p>
            <p>Segue o relatório dos processos que foram atualizados no dia {data}:</p>
            <p></p>
            <table>
                <thead>
                    <tr>
                        <th scope="col">REG</th>
                        <th scope="col">Cidade</th>
                        <th scope="col">Projeto</th>
                        <th scope="col">MD</th>
                        <th scope="col">Processo Judicial</th>
                        <th scope="col">Analista</th>
                    </tr>
                </thead>
                <tbody>
                    {linhas_tabela}
                </tbody>
                <tfoot>
                    <tr>
                        <th scope="row" colspan="5">Quantidade de Atualizações</th>
                        <td>{quantidade_atualizacoes}</td>
                    </tr>
                </tfoot>
            </table>
        </body>
        </html>'''

    else:
        corpo = f'''<html>
        <body>
            <p><b>Bom dia, Lia! Tudo bom?</b></p>
            <p>Não houve processos atualizados no dia {data}.</p>
        </body>
        </html>'''


    try:
        logger.info("Logando no e-mail")
        host = os.getenv("MAIL_HOST")
        port = os.getenv("MAIL_PORT")
        login = os.getenv("MAIL_LOGIN")
        senha = os.getenv("MAIL_SENHA")

        server = smtplib.SMTP(host, port)

        server.ehlo()
        server.starttls()
        server.login(login, senha)
    
    except Exception as e:
        logger.error(f"Não foi possível fazer login: {e}")

    try:
        logger.info("Tentando enviar e-mail")
        email = MIMEMultipart()
        email['From'] = os.getenv("MAIL_LOGIN")
        email['To'] = os.getenv("MAIL_LOGIN")
        email['Subject'] = f'Relatório de Atualizações do Diário da Justiça - {data}'
        email.attach(MIMEText(corpo, 'HTML'))

        server.sendmail(email['From'], email['To'], email.as_string())
        logger.info("E-mail enviado com sucesso.")
    
    except Exception as e:
        logger.error("Não foi possível enviar o e-mail: {e}")

    finally:
        server.close()

