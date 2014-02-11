import socket

hote = "localhost"
port = 12800

servCo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servCo.connect((hote, port))

msg = b""
while msg !=b"fin":
	msg = raw_input("> ")
	msg = msg.encode()
	servCo.send(msg)
	msgBack = servCo.recv(1024)
	print(msgBack.decode())

print("Fermeture de la connection")
servCo.close()
