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
import dbconsts
from datetime import datetime, timedelta

DEF_EVENT_TITLE = "Nouvel évènement"

#
# event - Un évènement du calendrier
#
class event(object):

    # Types d'évènement
    #
    EVENT_TYPE_NONE = 0
    EVENT_TYPE_REPOS = dbconsts.TYPE_REST
    EVENT_TYPE_ACTIVITE = dbconsts.TYPE_WORK
    EVENT_TYPE_PAUSE_MERIDIENNE = dbconsts.TYPE_MEAL_TIME
    EVENT_TYPE_SORTIE = dbconsts.TYPE_NIGHT_WORK
    EVENT_TYPE_RECUPERATION = dbconsts.TYPE_RECOVERY

    # Types de chevauchements
    #
    OVERLAP_NONE = 0
    OVERLAP_START_IN = 1
    OVERLAP_END_IN = 2
    OVERLAP_FULL = (OVERLAP_START_IN or OVERLAP_END_IN) # Même temporalité

    EVT_DURATION_MIN = 30      # Duréee min. d'un évènement

    # Construction
    def __init__(self, title = None, type = EVENT_TYPE_NONE, startDate = None, duration = 0):
        self.idEvent_ = options.ID_NEW   # Nouvel évènement
        self.title_ = title if title is not None else DEF_EVENT_TITLE
        self.idType = type
        self.userID_ = 0
        self.status_ = dbconsts.STATUS_OK
        self.startDate_ = startDate if startDate is not None else datetime.today()
        evtDuration = timedelta(minutes = duration if duration > self.EVT_DURATION_MIN else self.EVT_DURATION_MIN)
        self.endDate_ = self.startDate_ + evtDuration

    # Un nouvel évènement ?
    def isNew(self) -> bool:
        return True if self.id == options.ID_NEW else False

    # ID de l'évènement
    @property
    def id(self):
        return self.idEvent_
    @id.setter
    def id(self, newVal):
        if newVal != options.ID_NEW and newVal != self.idEvent_:
            self.idEvent_ = newVal

    # Type d'évènement
    @property
    def type(self):
        return self.idType_
    @type.setter
    def type(self, newType):
        if newType != self.EVENT_TYPE_NONE and newType != self.idType_:
            self.idType_ = newType

    # Statut de l'évènement
    @property
    def status(self):
        return self.status_
    @type.setter
    def type(self, newStatus):
        if newStatus != self.status_:
            self.status_ = newStatus

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
        return f"Objet : {"vide" if self.title_ == "" else self.title_}\n Du : {self.startDate_}\n Au : {self.endDate_}\n Type : {self.idType_}"

# EOF
