import socket
IP_Servidor = '127.0.0.1'             
PORTA_Servidor = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

DESTINO = (IP_Servidor, PORTA_Servidor) 
tcp.connect(DESTINO) 
Mensagem = ''
while Mensagem != '\x18':
    Mensagem = input("-> ")  
    tcp.send(bytes(Mensagem,"utf8")) 
tcp.close()
#para finalizar basta usar o CTRL+C ou CTRL+ X + enter