#!/usr/bin/python3
#
# coding=UTF-8
#
#   Fichier     :   calendar.py
#
#   Auteur      :   Jérôme Heny-Barnaudière - DSI
#
#   Description :   "Calendrier" d'un agent"
#

import event

#
# calendar - Calendrier professionel d'un agent
#
class calendar(object):

    ID_NO_USER = 0

    # Construction
    def __init__(self, agentID = 0):
        self.idAgent_ = agentID
        self.events_ = [] # Pas d'évènements pour cet agent

    # Ajout d'un évènement à une journée
    #
    #  Retourne {done ?, [evts]}
    def _addEvent(self, evt : event.event):
        if evt.type != event.event.EVENT_NONE :
            return True
        return False, None

    # Suppression de la liste des evènements
    def clear(self):
        self.events_ = []

    #
    # I/O
    #

    # Sauvegarde des évènements du calendrier en mémoire
    def __save(self) -> int:
        count = 0
        for evt in self.events_ :
            if evt.isNew():
                newID = self.__saveSingleEvent(evt)
                if newID != event.event.ID_NEW:
                    evt.id = newID
                    count+=1
        return count

    # Chargement de certains évènements du calendrier
    def __load(self):
        if len(self.events_) > 0:
            pass
        pass

    # Sauvegarde d'un seul élément
    def __saveSingleEvent(self, evt : event.event):
        return event.event.ID_NEW

    # Mise à jour d'un seul élément
    def __updateSingleEvent(self, evt : event.event):
        return event.event.ID_NEW


# EOF
