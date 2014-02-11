import socket

hote = ""
port = 12800

servCo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servCo.bind((hote, port))
servCo.listen(5)

clientCo, infosCC = servCo.accept()


msg = b""
while msg !=b"fin":
	msg = clientCo.recv(1024)
	print(msg.decode())
	clientCo.send(b"5/5")

print("Fermeture de la connection")
clientCo.close()
servCo.close()
