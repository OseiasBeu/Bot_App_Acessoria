# TO DO:
- [x] - Criação da classe Browser
- [x] - Criação da função openBrowser
- [x] - Criação da função de login
- [x] - Criação da função goToDeliveryList
- [x] - Criação da função searchDepartment
- [x] - Criação da função getRecords
- [x] - Criação do módulo get_env
- [x] - Criação da classe Email
- [x] - Criação da função send_email
- [x] - Criar módulo de verificação de pacotes
- [x] - Criar módulo de instalação de pacotes
- [x] - Criar agendador de evento para execução no periodo solicitado (SEG-SEX [07:30 AM & 16:30 PM])
- [x] - Criar arquivo requirements.txt
- [x] - Finalizar instruções do readme

---
# BUG:
- [x] - Entender como fazer o disparo de email utilizando o smtplib

---
# INSTRUÇÕES PARA USO:
- 1º: Antes de tudo, você vai precisar de uma senha para o disparo de emails com o script, para isso, consida a mesma segindo esse guia: [Link](https://github.com/OseiasBeu/Bot_App_Acessoria/blob/main/Assets/Guia%20para%20gerar%20a%20senha%20de%20app%20para%20disparo%20de%20email%20com%20python.pdf)

- 2º: Agora, você precisará criar o arquivo `.env` na pasta raiz do projeto;
- 3º: Adicionar as variáveis de execução: 

    >email='EMAIL DE LOGIN NO SITE DA ACESSORIA'

    >pwd='SENHA DE ACESSO AO SITE DA ACESSORIA'

    >senderEmail='EMAIL DO REMETENTE'

    >senderPwd='SENHA DO REMETENTE' (senha adiquirida na etapa 1)

    >to_fiscal='fiscal@dominio.com' - Alterar email
    
    >to_pessoal='pessoal@dominio.com' - Alterar email   
    
    >to_processos='processos@dominio.com' - Alterar email
    
    >to_contabil='contabil@dominio.com' - Alterar email

- 4º: Agora, faça a instalação dos pacotes: `pip install -r requirements.txt`

- 5º: Execute o programa com: `python main.py` 

OBS.: O BPA já está agendado para executar nos horários pré-definidos [07:30 & 17:30]


