import socket
import random
import time 

while True:
    HOST = '127.0.0.1'
    PORT = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """Realiza a conexão com o servidor"""
    s.connect((HOST, PORT))

    num_digitos= random.randint(1,30)
    inteiro = random.randint(10**(num_digitos-1), 10**num_digitos-1)
    print(f"Enviando {inteiro} para o servidor...\n")
    data = str(inteiro)
    """Envia data pro servidor"""
    s.sendall(data.encode())
    """Recebe data do servidor"""
    data = s.recv(1024).decode()
    print(data)
    print("\nFIM\n")
    print("Aguarde 10 segundos até a proxima conexão...\n")
    time.sleep(10)