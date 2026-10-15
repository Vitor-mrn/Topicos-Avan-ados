import logging
import azure.functions as func
<<<<<<< HEAD
import os
import pyodbc

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado(myTimer: func.TimerRequest) -> None:

    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")


    #criar a conexao com o banco de dados
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={host};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    try:
        # Estabelece a conexão
        conn = pyodbc.connect(conn_str)

        logging.info("Conexão com o banco estabelecida com sucesso.")

        # Cria o cursor
        cursor = conn.cursor()

        # Executa o SELECT
        query = """
            SELECT TOP 10 *
            FROM itsm.chamado
        """

        cursor.execute(query)

        # Recupera os registros
        rows = cursor.fetchall()

        # Exibe os resultados no log
        for row in rows:
            logging.info(row)

        # Fecha cursor e conexão
        cursor.close()
        conn.close()

        logging.info(f"Total de registros encontrados: {len(rows)}")

    except pyodbc.Error as e:
        logging.error(f"Erro no banco de dados: {e}")
        raise
=======

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * /15 * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    usuario = os.getenv("USER")
    senha = os.getenv("password")
    database = os.getenv("BDA")
    HOST = os.getenv("lider")
    print(usuario)  
    print(password)              
    print(lider)
    print(BDA)
>>>>>>> b8bbb47b056906fccfb309fbc82d9d63aa49a49d
