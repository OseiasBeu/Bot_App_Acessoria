import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class Email():
    def __init__(self) -> None:
        self.host = 'smtp.gmail.com'
        self.port = 587

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
            email_msg['Subject'] = 'QUANTIDADE DE REGISTROS'
            email_msg.attach(MIMEText(message[0], 'plain'))

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
    qtdRecords = 15
    message = f'A quantidade de registros é:{qtdRecords}'
    envs = {}
    envs['senderEmail'] = 'SEU EMAIL VAI AQUI'
    envs['senderPwd'] = 'SUA SENHA VAI AQUI'
  
    email.send_email(envs['senderEmail'],envs['senderPwd'],'AQUI VAI O EMAIL DO RECEBEDOR',[message,'Quantidade de Registros'])