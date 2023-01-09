import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from datetime import datetime

class Email():
    def __init__(self) -> None:
        self.host = 'smtp.gmail.com'
        self.port = 587
        
    def setMensage(self, departamento, qtdRecords):
        try:
            logging.info('Iniciando a configuração da mensagem ...')
            curr_datetime = datetime.now()
            hour = curr_datetime.hour
            
            if hour < 12:
                subject = f'Obrigações vencendo hoje: {qtdRecords}'
                body_email = f'''
                Olá amigos do departamento {departamento}, vocês possuem {qtdRecords} obrigações vencendo hoje.
                Fiquem atentos para não perder nenhum prazo.
                
                Este e-mail é enviado de forma automática, não responda!
                '''
                logging.info('Mensagem padrão de antes do meio dia!')
            else:
                logging.info('Configuração daapós o meio dia!')
                if int(qtdRecords) > 0:
                    subject = f'Atenção, ainda constam: {qtdRecords} obrigações vencendo hoje'
                    body_email = f'''
                    Olá amigos do departamento {departamento}, vocês possuem {qtdRecords} obrigações vencendo hoje.
                    Fiquem atentos para não perder nenhum prazo.
                    
                    Este e-mail é enviado de forma automática, não responda!
                    '''
                    logging.info(f'Mensagem para depois do meio dia, com {qtdRecords} registros')
                elif int(qtdRecords) == 0:
                    subject = f'Parabéns, Todas as obrigações foram entregues!'
                    body_email = f'''Olá amigos do departamento {departamento},
                    Parabéns! Vocês já realizaram todas as entregas previstas para hoje!
                    
                    Este e-mail é enviado de forma automática, não responda!
                    '''
                    logging.info(f'Mensagem para depois do meio dia, com {qtdRecords} registros')
                    
            return [subject, body_email]
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')  
            
            

    def send_email(self,senderEmail,senderPwd,to,message):
        try:
            logging.info('Criando objeto servidor...')
            server = smtplib.SMTP(self.host, self.port)
            logging.info('Efetuando login')
            server.ehlo()
            server.starttls()
            server.login(senderEmail, senderPwd)
            
            logging.info('Preparando email')
            email_msg = MIMEMultipart()
            email_msg['From'] = senderEmail
            email_msg['To'] = to
            email_msg['Subject'] = message[0]         
            
            email_msg.attach(MIMEText(message[1], 'plain'))

            logging.info('Enviando email')
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            logging.info('Email enviado!')
            server.quit()
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')

            
if __name__ == "__main__":
    email = Email()
    message = email.setMensage('Fiscal', 43)

    envs = {}
    envs['senderEmail'] = 'SEU EMAIL VAI AQUI'
    envs['senderPwd'] = 'SUA SENHA VAI AQUI'
    email.send_email(envs['senderEmail'],envs['senderPwd'],'AQUI VAI O EMAIL DO RECEBEDOR',[message,'Quantidade de Registros'])

