#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Etienne LAFARGE - Janvier 2014 
École Nationale Supérieure des Mines de Paris
Projet Vector - vDrive - Poste de pilotage, aide au pilotage, pilote automatique pour un prototype électrique
"""

import socket
import threading
import select

class Serveur(threading.Thread):
    """ Classe abstraite désignant un serveur de données quelquconques, toute classe fille devra implémenter la méthode _encoderDonnees et decoderDonnees (statique) qui seront appelées respectivement par le serveur lorsqu'on lui demande un envoi de données en particulier et par un client codé en Python qui voudra récupérer facilement l'objet de données renvoyé. Toute implémentation de client dans un autre langage devra prendre en charge le décodage elle-même. L'utilisation d'envois en JSON est fortement conseillée pour faciliter le décodage"""

    def __init__(self, nom, hote = '', port = 12800):
        """ Construit un serveur qui va fournir els données issues d'un capteur quelconque """
        self._hote = hote
        self._port = port
        self._nom = nom
        self._clients = []
        self._terminateThread = False
        threading.Thread.__init__(self)

    def stop(self):
        self._terminateThread = True
        print("Le serveur de {0} a été sommé de s'arrêter.".format(self._nom))

    def run(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((self._hote, self._port))
        self._sock.listen(5)
        print("Le serveur de {0} est prêt à fournir les données issues de ses capteurs associés sur le port {1}.".format(self._nom, self._port))

        while not self._terminateThread:
            requests, wlist, xlist = select.select([self._sock], [], [], 0.05)

            for request in requests:
                conClient, infosCon = request.accept()
                self._clients.append(conClient)

            clientsEnAttente = []
            try:
                clientsEnAttente, wlist, xlist = select.select(self._clients, [], [], 0.05)
            except select.error:
                pass
            else:
                for client in clientsEnAttente:
                    msg = client.recv(1024)
                    msg = msg.decode()

                    client.send(self._encoderDonnees())

        for client in self._clients:
            client.close()

        print("Le serveur de {0} s'est arrêté correctement.".format(self._nom))

    def _encoderDonnees(self):
        """ Méthode abstraite à définir dans les classes fille """
        return

    def decoderDonnes(donnees):
        return

