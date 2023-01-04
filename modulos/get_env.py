#!/usr/bin/env python3
import os
import logging
import dotenv

def print_env(body):
    try:
        logging.info('Efetuando leitura de variáveis de login.')
        dotenv.load_dotenv()
        dict = {}
        for field in body:
            dict[field] = os.getenv(field)

        logging.info('Finalizando leitura de variáveis de login.')
        return dict
    except Exception as e:
        logging.error('==========| ERRO |==========')
        logging.error(f'Um erro inesperado aconteceu: {e}')
        logging.error('==========| ERRO |==========')

if __name__ == "__main__":
    body = ['email']
    print_env(body)