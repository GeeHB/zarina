#!/usr/bin/python3
#
# coding=UTF-8
#
#   Fichier     :   zarina.py
#
#   Auteur      :   Jérôme Heny-Barnaudière - DSI
#
#   Description :   Gestion des sorties aléataoires et des repos associés
#

from activity import calendar, calendarException
import event


# Point d'entrée
if '__main__' == __name__:
    try:
        calendrier = calendar()
        calendrier._connect()

    except calendarException as excpt:
        print(excpt)


# EOF
