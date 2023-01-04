from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import logging

class Email:
    def __init__(self):
        pass
    
    def send_email(self, sender, pwd, receivers, body):
        try:
            logging.info('Iniciando envio de email')
            sender = sender
            receivers = receivers
            message = body[0]
            subject = body[1]
            
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(receivers)
            smtp_server = SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login(sender, pwd)
            smtp_server.sendmail(sender, receivers, msg.as_string())
            smtp_server.quit()   
            logging.info('Email enviado com sucesso!')
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')


if __name__ == "__main__":
    email = Email()
    message = f'A quantidade de registros é: 123'
    email.send_email('EMAIL_REMETENTE_AQUI','SENHA',['EMAIL_DESTINATÁRIO_AQUI'],[message,'Quantidade de Registros'])
    