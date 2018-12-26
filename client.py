import socket
serverIp = '127.0.0.1'
serverPort = 12000
BUFFER_SIZE =1024
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
opp = ['+','-','*','/']
while 1:
    x = input("Input first number: ")
    y = input("Input second number: ")
    operation = input("Input operation(+,-,*,/): ")
    if operation == '+': operation = 'add'
    if operation == '+': operation = 'add'
    if operation == '-': operation = 'sub'
    if operation == '*': operation = 'mul'
    if operation == '/': operation = 'div'
    message = operation+" "+x+" "+y
clientSocket.sendto(message.encode('utf-8'),(serverIp,serverPort))
response, address =clientSocket.recvfrom(BUFFER_SIZE)
print(message+'=' +response.decode('utf-8'))
clientSocket.close()
