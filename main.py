import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

dicionario = (requisicao.json())
cotacao = float(dicionario ['USDBRL']['high']) 
print (cotacao)

import smtplib
import email.message

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Cotação atual: R${cotacao}.Hora de comprar. </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "O Dólar está no precinho"
    msg['From'] = 'contaparacodigo1@gmail.com'
    msg['To'] = 'contaparacodigo1@gmail.com, danielaugustohgd@gmail.com'
    password = 'ldimnkktemvupake'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao <= 5.30:
    enviar_email(cotacao)
