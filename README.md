# Conexão Cliente-Servidor Sockets

Trabalho introdutorio a Socket disciplina de redes de computadores

## Status do Projeto

Concluido

## Como executar

Executar os arquivos em ordem

servidor.py e em seguida cliente.py em terminais diferentes

## Funções do projeto

Servidor.py
1. O programa servidor irá esperar a conexão de clientes;
2. Recebe o número;
3. Se o número tiver mais de 10 casas, gera e envia uma string do mesmo
tamanho para o cliente;
4. Se for menor que 10, verifica se é par ou ímpar e envia “PAR” ou “ÍMPAR” para
o cliente. 

cliente.py
1. O programa cliente irá se conectar ao servidor;
2. Gerar um número inteiro com até 30 casas;
3. Enviar esse número para o servidor;
4. Deve receber, imprimir no console e devolver o valor recebido do servido + “FIM”
5. Fecha a conexão
6. Repete a cada 10 segundo

## Explicação de como funciona

No arquivo servidor.py, quando executado, cria-se um objeto do tipo socket e define suas propriedades, como o tipo da conexão (se é TCP ou UDP), iniciando em seguida as conexões do lado servidor, 
que verifica se o cliente foi conectado.

 Então no arquivo cliente.py, quando executado, solicita conexão como cliente com o lado servidor, após aprovado ele gera e envia um inteiro aleatório de até 30 casas, o servidor então recebe e verifica, caso o inteiro seja menor que 10 o servidor retornará se ele é par ou impar ao cliente, mas caso seja maior que 10 o lado do servidor gera uma string aleatória de mesmo tamanho e retorna ao lado cliente, que por sua vez, independente do retorno do lado servidor, imprime o retorno e a string "FIM".  Após 10 segundos toda a conexão via socket é repetida.

Em síntese, o programa realiza os seguintes passos;
1- Servidor se conecta ao Cliente
2- Cliente envia um número inteiro aleatório de no máximo 30 casas
3- Servidor verifica se esse número é menor que 10, se for, verifica se é ímpar ou par, se não, gera uma string aleatória de mesmo tamanho.
4- Servidor retorna pro Cliente o resultado do passo número três. 
5- o Cliente imprime na tela o que foi retornado mais a string "FIM". 

Com o adendo de que, todas as trocas de informações são impressas ou do lado do cliente, ou do lado do servidor, de modo a deixar a troca de dados mais evidente.

## Tecnoplogias Utilizadas

As seguintes ferramentas foram usadas na construção do projeto

- [Linguagem Python](https://www.python.org/)

- [IDE Visual Studio Code](https://code.visualstudio.com/)

## Autores 

Hanna Lopes Correia de Oliveira : hannalopes@alu.ufc.br

José Mateus Mendonça Porto :  jmateusmp78@alu.ufc.br

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
