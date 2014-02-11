#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Etienne LAFARGE - Janvier 2014 
École Nationale Supérieure des Mines de Paris
Projet Vector - vDrive - Poste de pilotage, aide au pilotage, pilote automatique pour un prototype électrique
"""

import Serveur

class ServeurVitesse(Serveur.Serveur):
    """ Classe encapsulant le serveur de vitesse. Cette classe surveille le port GPIO sur lequel est branché le capteur de vitesse et tiens à jour des informations de vitesse et de position (par indentation), elle envoie à quiconque lui demande la dernière vitesse calculée ainsi que la vitesse moyenne sur le tour et la position """
    def __init__(self):
        Serveur.Serveur.__init__(self, "vitesse", '', 12800)
        self.start()
        self._vitesse = 12.3
        self._startSensing()
        
    def _startSensing(self):
        return

    def _encoderDonnees(self):
        return ("{0}".format(self._vitesse)).encode()

    def decoderDonnees(donnees):
        return donnees

if __name__ == "__main__":
    serv = ServeurVitesse()

