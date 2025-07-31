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

from datetime import datetime, timedelta

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

    # Types de chevauchements
    #
    OVERLAP_NONE = 0
    OVERLAP_LEFT = 1
    OVERLAP_RIGHT = 2
    OVERLAP_FULL = (OVERLAP_LEFT or OVERLAP_RIGHT) # Même temporalité

    ID_NEW = 0

    EVT_DURATION_MIN = 30      # Duréee min. d'un évènement

    # Construction
    def __init__(self, title = None, type = EVENT_NONE, startDate = None, duration = 0):
        self.idEvent_ = self.ID_NEW   # Nouvel évènement
        self.title_ = title if title is not None else DEF_EVENT_TITLE
        self.typeEvent_ = type
        self.modified_ = False
        self.startDate_ = startDate if startDate is not None else datetime.today()
        evtDuration = timedelta(minutes = duration if duration > self.EVT_DURATION_MIN else self.EVT_DURATION_MIN)
        self.endDate_ = self.startDate_ + evtDuration

    # Un nouvel évènement ?
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

    # L'evt a t'il été modifié ?
    @property
    def modified(self):
        return self.modified_
    @modified.setter
    def modified(self, changed):
        if changed != self.modified_:
            self.modified_ = changed

    # L'evt a t'il un chevauchement avec l'evt courant ?
    def overlap(self, other) :
        if type(self) != type(other):
            return False, self.OVERLAP_NONE

        tOverlap = self.OVERLAP_NONE

        if self.startDate_ <= other.startDate_ :
            tOverlap |= self.OVERLAP_LEFT

        if self.endDate_ >= other.endDate_:
            tOverlap |= self.OVERLAP_RIGHT

        return True, tOverlap

# EOF
