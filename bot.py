import pywhatkit
import time

while True:
    mensagem = input("Digite sua mensagem (ou 'sair' para fechar): ")
    if mensagem.lower() == 'sair':
        break
    
    numero = input("Digite o número do destinatário (com DDD e código do país, ex: +5583987654321): ")
    
    # Envia a mensagem (ajuste a hora para 1 minuto no futuro)
    pywhatkit.sendwhatmsg(numero, mensagem, time.localtime().tm_hour, time.localtime().tm_min + 1)
    
    print("Mensagem enviada com sucesso!")
