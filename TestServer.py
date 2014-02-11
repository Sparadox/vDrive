import socket

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.bind(('', 12800))
connexion.listen(5)

coClient,infosCo = connexion.accept()

while True:
	msg = coClient.recv(1024)
	print(msg.decode())
	coClient.send("ok")
