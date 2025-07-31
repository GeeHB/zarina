#!/usr/bin/python3
#
# coding=UTF-8
#
#   Fichier     :   activity.py
#
#   Auteur      :   Jérôme Heny-Barnaudière - DSI
#
#   Description :   "Calendrier" d'un agent"
#

import options
import event

#
# Exception lors des traitements
#
class calendarException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

    def __repr__(self):
        return f"{options.APP_TITLE} : {self.message}"

#
# activity - Calendrier professionel d'un agent
#
class activity(object):

    ID_NO_USER = 0

    # Construction
    def __init__(self, agentID = 0):
        self.idAgent_ = agentID
        self.events_ = [] # Pas d'évènements pour cet agent

    # Ajout d'un évènement à une journée
    #
    #  Retourne {done ?, [evts]}
    def _addEvent(self, evt : event.event):
        if evt.type != event.event.EVENT_TYPE_NONE :
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
