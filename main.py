import sys,logging, schedule

sys.path.append('modulos')
from browser import Browser
from get_env import print_env
from mail import Email


LOG_FILENAME = 'logs\log.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8', mode='w+')],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def job():
    try:
        logging.info('==========| INICIANDO BPA |==========')
        navegador = Browser()
        navegador.openBrowser()
        email = Email()
        
        envs = print_env(['email','pwd','senderEmail','senderPwd','to_fiscal','to_pessoal','to_processos','to_contabil'])
        navegador.login(envs['email'],envs['pwd'])
        navegador.goToDeliveryList()
        navegador.setDate()
        
        navegador.searchDepartment('Fiscal')
        qtdRecords = navegador.getRecords()
        # qtdRecords= qtdRecords.replace('[','').replace(']','')
        
        message = email.setMensage('Fiscal', qtdRecords)
        email.send_email(envs['senderEmail'],envs['senderPwd'],envs['to_fiscal'],message)
        
        navegador.searchDepartment('Pessoal')
        qtdRecords = navegador.getRecords()
        # qtdRecords= qtdRecords.replace('[','').replace(']','')
        
        message = email.setMensage('Pessoal', qtdRecords)
        email.send_email(envs['senderEmail'],envs['senderPwd'],envs['to_pessoal'],message)
        
        navegador.searchDepartment('Processos')
        qtdRecords = navegador.getRecords()
        # qtdRecords= qtdRecords.replace('[','').replace(']','')
        
        message = email.setMensage('Processos', qtdRecords)
        email.send_email(envs['senderEmail'],envs['senderPwd'],envs['to_processos'],message)
        
        navegador.searchDepartment('Contábil')
        qtdRecords = navegador.getRecords()
        # qtdRecords= qtdRecords.replace('[','').replace(']','')
        
        message = email.setMensage('Contábil', qtdRecords)
        email.send_email(envs['senderEmail'],envs['senderPwd'],envs['to_contabil'],message)

        
        logging.info('==========| FINALIZANDO BPA |==========')
    except Exception as e:
        logging.error('==========| ERRO |==========')
        logging.error(f'Um erro inesperado aconteceu: {e}')
        logging.error('==========| ERRO |==========')


if __name__ == "__main__":
    logging.info('BPA agendado para execução')
    schedule.every().day.at("07:28").do(job)
    schedule.every().day.at("16:28").do(job)

    while True:
        schedule.run_pending()

    # logging.info('Fim do BPA')
    