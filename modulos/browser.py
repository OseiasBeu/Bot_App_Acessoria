from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
import logging

from get_env import print_env


class Browser:
    def __init__(self):
        logging.info('Instanciando browser')
        options = Options()
        options.add_argument('lang=pt-br')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)
        self.by = By
        self.keys = Keys
        self.paginaLogin = 'https://app.acessorias.com/index.php'
    
    def openBrowser(self):
        logging.info('Abrindo Navegador')
        self.driver.get(self.paginaLogin)
    
    def login(self,email,pwd):
        try:
            logging.info('Efetuando login')
            inputEmail = self.driver.find_element(self.by.XPATH,'//*[@id="site-corpo"]/section[1]/div/form/div[1]/div[1]/input')
            inputEmail.send_keys(email)
            
            inputPwd = self.driver.find_element(self.by.XPATH,'//*[@id="site-corpo"]/section[1]/div/form/div[1]/div[2]/input')
            inputPwd.send_keys(pwd)        
            
            buttonLogin = self.driver.find_element(self.by.XPATH,'//*[@id="site-corpo"]/section[1]/div/form/div[2]/button')
            buttonLogin.submit()
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')
               
        
    def goToDeliveryList(self):
        try:
            time.sleep(7)
            logging.info('Entrando no menu Lista de Entregas')
            self.driver.find_element(self.by.XPATH,'//*[@id="M3"]/a/span').click()
            logging.info('Página Lista de Entregas processada...')
            
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')
            
    def searchDepartment(self,departament):
        try:
            logging.info(f'Efetuando busca pelo departamento:{departament}')
            filterDepartament = self.driver.find_element(self.by.XPATH,'//*[@id="fieldFilters"]/span/span[1]/span/ul/li/input')
            clearFilter = self.driver.find_element(self.by.XPATH,'//*[@id="fieldFilters"]/span/span[1]/span/ul/li[1]/span')            
            clearFilter.click()
            filterDepartament.click()
            departament = 'Dpto: ' + departament
            filterDepartament.send_keys(departament)  
            filterDepartament.send_keys(self.keys.ENTER)  
            time.sleep(3)
            logging.info(f'Busca realizada com sucesso.')
            
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')

    def getRecords(self):
        try:
            logging.info(f'Capturando a quantidade de registros')
            qtdRecords = self.driver.find_element(By.XPATH, '//*[@id="entTotReg"]').text
            time.sleep(3)
            logging.info(f'Captura de registros efetuada com sucesso! QTD.: {qtdRecords}')
            return qtdRecords 
        except Exception as e:
            logging.error('==========| ERRO |==========')
            logging.error(f'Um erro inesperado aconteceu: {e}')
            logging.error('==========| ERRO |==========')           

        
if __name__ == "__main__":
    navegador = Browser()
    navegador.openBrowser()
    envs = print_env(['email','pwd'])
    navegador.login(envs['email'],envs['pwd'])
    navegador.goToDeliveryList()
        