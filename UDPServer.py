from socket import *

serverPort = 7171
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The UDP server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    sentence = message.decode().strip()

    # Try to check if input is a number
    if sentence.isdigit() or (sentence.startswith('-') and sentence[1:].isdigit()):
        number = int(sentence)
        if number % 2 == 0:
            reply = f"{number} is even"
        else:
            reply = f"{number} is odd"
    else:
        reply = "Please send a valid integer."

    serverSocket.sendto(reply.encode(), clientAddress)









