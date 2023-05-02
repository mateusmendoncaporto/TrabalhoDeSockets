
import socket
import random

HOST = 'localhost'
PORT = 5000

"""criar um objeto do tipo socket com endereço ipv4 com socket TCP"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""iniciando a escuta de conexões no lado do servidor."""
s.bind((HOST, PORT))

"""controle de conexões simultâneas que o servidor suportará"""
s.listen()
print ('Aguardando conexão de um cliente...')

while True:
    """aceita novas conexões"""
    conn, ender = s.accept()

    print ('Conectado em ', ender)

    while True:
        """Recebe os dados, nesse caso dentro da váriavel data"""
        data = conn.recv(1024)
        if not data:
            print ('Fechando a conexão')
            conn.close()
            break
        """Coverte o dado em inteiro"""
        inteiro = int(data)
        print(f'Recebido o inteiro: {inteiro}')
        """verifica se o inteiro é par ou impar caso seja menor que 10"""
        if inteiro < 10:
            if inteiro % 2 == 0:
                data = "PAR"
            else:
                data = "IMPAR"
            """Envia a string gerada pelo servidor pro cliente"""
            print(f"Enviando {data} para o cliente.")
            conn.send(data.encode())
        else:
            """Gera uma string aleatória e envia pro cliente"""
            tamanho = str(inteiro)
            data = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(len(tamanho)))
            print(f"Enviando {data} para o cliente.")
            conn.send(data.encode())

        