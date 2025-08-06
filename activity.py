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

import mariadb
import dbconsts

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
# calendar - Calendrier professionel d'un agent
#
class calendar(object):

    ID_NO_USER = 0

    # Construction
    def __init__(self, agentID = options.ID_NEW):

        self.idAgent_ = agentID

        # DB
        self.conn_ = None
        self.cur_ = None

        if options.ID_NEW != agentID:
            self.load()
        else:
            self.events_ = [] # Pas d'évènements pour cet agent

    # Destruction
    def __del__(self):
        self._disconnect()

    # Ajout d'un évènement à une journée
    #
    #  Retourne {done ?, [evts]}
    def addEvent(self, evt : event.event):
        if evt.type != event.event.EVENT_TYPE_NONE :
            return True
        return False, None

    # Suppression de la liste des evènements
    def clear(self):
        self.events_ = []

    #
    # I/O
    #

    # Connection à la base de données
    def _connect(self) -> bool:
        if self.conn_ is None :
            try:
                self.conn_ = mariadb.connect(
                        host=dbconsts.DB_HOST,
                        port=dbconsts.DB_PORT,
                        database=dbconsts.DB_NAME,
                        user=dbconsts.DB_USER,
                        password=dbconsts.DB_PWD,
                        connect_timeout = dbconsts.DB_CONNECT_TIMEOUT)
            except mariadb.Error as e:
                print(f"Erreur de connexion à la base de données : \"{e}\"")
                self.conn_ = None

        return (self.conn_ is not None)

    # Deconnection
    def _disconnect(self):
        if self.cur_ is not None:
            self.cur_.close()
            self.cur_ = None

        if self.conn_ is not None:
            self.conn_.close()
            self.conn_ = None

    # Sauvegarde des évènements du calendrier en mémoire
    def save(self) -> int:
        count = 0
        for evt in self.events_ :
            if evt.isNew():
                newID = self.__saveSingleEvent(evt)
                if newID != options.ID_NEW:
                    evt.id = newID
                    count+=1
        return count

    # Chargement de certains (ou de tous les) évènements du calendrier
    def load(self, start = None):
        if len(self.events_) > 0:
            self.clear()

    # Sauvegarde d'un seul élément
    def __saveSingleEvent(self, evt : event.event):
        return options.ID_NEW

    # Mise à jour d'un seul élément
    def __updateSingleEvent(self, evt : event.event):
        return options.ID_NEW


# EOF
