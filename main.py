import sys,logging, time

sys.path.append('modulos')
from browser import Browser
from get_env import print_env
from mail import Email


# secret = print_env(body)

LOG_FILENAME = 'logs\log.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8', mode='w+')],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

try:
    logging.info('==========| INICIANDO BPA |==========')
    navegador = Browser()
    navegador.openBrowser()
    email = Email()
    
    envs = print_env(['email','pwd','senderEmail','senderPwd'])
    navegador.login(envs['email'],envs['pwd'])
    navegador.goToDeliveryList()
    
    navegador.searchDepartment('Fiscal')
    qtdRecords = navegador.getRecords()
    message = f'A quantidade de registros é:{qtdRecords}'
    email.send_email(envs['senderEmail'],envs['senderPwd'],['fiscal@dominio.com'],[message,'Quantidade de Registros'])
    
    navegador.searchDepartment('Pessoal')
    qtdRecords = navegador.getRecords()
    message = f'A quantidade de registros é:{qtdRecords}'
    email.send_email(envs['senderEmail'],envs['senderPwd'],['pessoal@dominio.com'],[message,'Quantidade de Registros'])
    
    navegador.searchDepartment('Processos')
    qtdRecords = navegador.getRecords()
    message = f'A quantidade de registros é:{qtdRecords}'
    email.send_email(envs['senderEmail'],envs['senderPwd'],['processos@dominio.com'],[message,'Quantidade de Registros'])
    
    navegador.searchDepartment('Contábil')
    qtdRecords = navegador.getRecords()
    message = f'A quantidade de registros é:{qtdRecords}'
    email.send_email(envs['senderEmail'],envs['senderPwd'],['contabil@dominio.com'],[message,'Quantidade de Registros'])
    
    time.sleep(5)
    
    logging.info('==========| FINALIZANDO BPA |==========')
except Exception as e:
    logging.error('==========| ERRO |==========')
    logging.error(f'Um erro inesperado aconteceu: {e}')
    logging.error('==========| ERRO |==========')
    