#!/usr/bin/python3
#
# coding=UTF-8
#
#   Fichier     :   dbconsts.py
#
#   Auteur      :   Jérôme Heny-Barnaudière - DSI
#
#   Description :   Constantes pour les accès à la base de données
#

# Accès
#
DB_HOST = "zarinaDB"
DB_NAME = "SortiesAleatoires"
DB_PORT = 3306
DB_USER = "localAdmin"
DB_PWD = "Scala_0392"

#
# Schéma
#

DB_USER_TABLE   = "user"
DB_USER_ID      = "idUser"
DB_USER_PROFIL  = "idProfil"
DB_USER_FNAME   = "prenom"
DB_USER_FNAME   = "name"

DB_EVENT_TABLE  = "event"
DB_EVENT_ID     = "idEvent"
DB_EVENT_USER   = "idAgent"
DB_EVENT_TYPE   = "idType"
DB_EVENT_TITLE  = "liebelle"
DB_EVENT_START  = "debut"
DB_EVENT_LAST   = "duree"
DB_EVENT_STATUS = "etat"

EVENT_TYPE_REST = 0
EVENT_TYPE_WORK = 1
EVENT_TYPE_MEAL_TIME = 2

DB_TYPE_TABLE   = "type"
DB_TYPE_ID      = "idType"
DB_TYPE_TITLE   = "libelle"

# Messages d'erreur
#
DB_ERROR_ = "hello"

#  EOF
