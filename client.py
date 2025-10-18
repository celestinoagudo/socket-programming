from socket import *
serverName = '124.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('input lowercase sentence: ').encode('utf-8')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print((modifiedMessage).decode('utf-8'))

clientSocket.close()


