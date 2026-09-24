import logging
import azure.functions as func

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