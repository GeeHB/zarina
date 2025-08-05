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

import options
from datetime import datetime, timedelta

DEF_EVENT_TITLE = "Nouvel évènement"

#
# event - Un évènement du calendrier
#
class event(object):

    # Types d'évènement
    #
    EVENT_TYPE_NONE = 0
    EVENT_TYPE_ACTIVITE = 1
    EVENT_TYPE_REPOS = 2
    EVENT_TYPE_PAUSE_MERIDIENNE = 3
    EVENT_TYPE_SORTIE = 4

    # Types de chevauchements
    #
    OVERLAP_NONE = 0
    OVERLAP_START_IN = 1
    OVERLAP_END_IN = 2
    OVERLAP_FULL = (OVERLAP_START_IN or OVERLAP_END_IN) # Même temporalité

    EVT_DURATION_MIN = 30      # Duréee min. d'un évènement

    # Construction
    def __init__(self, title = None, type = EVENT_TYPE_NONE, startDate = None, duration = 0):
        self.idEVENT_TYPE_ = options.ID_NEW   # Nouvel évènement
        self.title_ = title if title is not None else DEF_EVENT_TITLE
        self.typeEVENT_TYPE_ = type
        self.modified_ = False
        self.startDate_ = startDate if startDate is not None else datetime.today()
        evtDuration = timedelta(minutes = duration if duration > self.EVT_DURATION_MIN else self.EVT_DURATION_MIN)
        self.endDate_ = self.startDate_ + evtDuration

    # Un nouvel évènement ?
    def isNew(self) -> bool:
        return True if self.id == options.ID_NEW else False

    # ID de l'évènement
    @property
    def id(self):
        return self.idEVENT_TYPE_
    @id.setter
    def id(self, newVal):
        if newVal != options.ID_NEW and newVal != self.idEVENT_TYPE_:
            self.idEVENT_TYPE_ = newVal

    # Type d'évènement
    @property
    def type(self):
        return self.typeEVENT_TYPE_
    @type.setter
    def type(self, newType):
        if newType != self.EVENT_TYPE_NONE and newType != self.typeEVENT_TYPE_:
            self.typeEVENT_TYPE_ = newType

    # L'evt a t'il été modifié ?
    @property
    def modified(self):
        return self.modified_
    @modified.setter
    def modified(self, changed):
        if changed != self.modified_:
            self.modified_ = changed

    # Durée en min. d'un évènement
    def duration(self) -> int:
        evtDuration = self.endDate_ - self.startDate_
        return int(evtDuration.total_seconds() / 60.0)

    # L'evt a t'il un chevauchement avec l'evt courant ?
    def overlap(self, other) :
        if type(self) != type(other):
            return False, self.OVERLAP_NONE

        tOverlap = self.OVERLAP_NONE

        if self.startDate_ <= other.startDate_ and self.endDate_ >= other.startDate_:
            tOverlap |= self.OVERLAP_START_IN

        if self.endDate_ >= other.endDate_ and self.startDate_ <= other.endDate_:
            tOverlap |= self.OVERLAP_END_IN

        return True, tOverlap

    #
    # Surcharges
    #

    # "==" - Les éléments sont-ils égaux (du point de vue du calendrier ...) ?
    def __eq__(self, other) -> bool:
        #return self.overlap(other) == self.OVERLAP_FULL and self.duration() == other.duration()
        return self.startDate_ == other.startDate_ and self.endDate_ == other.endDate_

    # Affichage de l'objet
    #
    def __repr__(self) -> str:
        return f"Objet : {"vide" if self.title_ == "" else self.title_}\n Du : {self.startDate_}\n Au : {self.endDate_}\n Type : {self.typeEVENT_TYPE_}"

# EOF
