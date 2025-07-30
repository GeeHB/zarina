#!/usr/bin/python3
#
# coding=UTF-8
#
#   Fichier     :   event.py
#
#   Auteur      :   Jérôme Heny-Barnaudière - DSI
#
#   Projet      :
#
#   Description :   Un évènement du calendrier : sortie, repos, ...
#

DEF_EVENT_TITLE = "Nouvel évènement"

#
# event - Un évènement du calendrier
#
class event(object):

    # Types d'évènement
    #
    EVENT_NONE = 0
    EVENT_ACTIVITE = 1
    EVENT_REPOS = 2
    EVENT_PAUSE_MERIDIENNE = 3
    EVENT_SORTIE = 4

    ID_NEW = 0

    # Construction
    def __init__(self, title = None, type = EVENT_NONE, startDate = None, startHour = None, duration = 0):
        self.idEvent_ = self.ID_NEW   # Nouvel évènement
        self.title_ = title if title is not None else DEF_EVENT_TITLE
        self.typeEvent_ =type


    # un nouvel évènement ?
    def isNew(self) -> bool:
        return True if self.id == self.ID_NEW else False

    # ID de l'évènement
    @property
    def id(self):
        return self.idEvent_
    @id.setter
    def id(self, newVal):
        if newVal != self.ID_NEW and newVal != self.idEvent_:
            self.idEvent_ = newVal

    # Type d'évènement
    @property
    def type(self):
        return self.typeEvent_
    @type.setter
    def type(self, newType):
        if newType != self.EVENT_NONE and newType != self.typeEvent_:
            self.typeEvent_ = newType

# EOF
