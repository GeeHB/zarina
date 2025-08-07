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
import event, dbconsts


# Point d'entrée
if '__main__' == __name__:
    try:
        calendrier = calendar()
        if False == calendrier.connect():
            exit(1)

        print(f"Connexion à la base '{dbconsts.DB_HOST}'")

        calendrier.clearUserEvents(15)

        evt = event.event("Vacances", event.event.EVENT_TYPE_REPOS, duration = 60, userID = 15)
        evt2 = event.event("Hello", event.event.EVENT_TYPE_REPOS, duration = 60, userID = 15)

        calendrier.addEvent(evt)
        calendrier.addEvent(evt2)

        print(f"{calendrier.save()} évènement(s) ajouté(s)")

        if calendrier.disconnect():
            print(f"Deconnexion à la base '{dbconsts.DB_HOST}'")
    except calendarException as excpt:
        print(excpt)


# EOF
