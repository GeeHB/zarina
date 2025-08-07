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
DB_CONNECT_TIMEOUT = 10     # in sec.

#
# Schéma
#

DB_USERS_TABLE   = "users"
DB_USERS_ID      = "idUser"
DB_USERS_PROFIL  = "idProfil"
DB_USERS_FNAME   = "prenom"
DB_USERS_FNAME   = "name"

DB_EVENTS_TABLE  = "events"
DB_EVENTS_ID     = "idEvent"
DB_EVENTS_USERID = "idAgent"
DB_EVENTS_TYPE   = "idType"
DB_EVENTS_TITLE  = "libelle"
DB_EVENTS_START  = "debut"
DB_EVENTS_LAST   = "duree"
DB_EVENTS_STATUS = "etat"

STATUS_OK           = 0
STATUS_JUST_ADDED   = 1
STATUS_TO_DELETE    = 2
STATUS_MODIFIED     = 3

DB_TYPE_TABLE   = "types"
DB_TYPE_ID      = "idType"
DB_TYPE_TITLE   = "libelle"

TYPE_UNKOWNN    = 0
TYPE_REST       = 1
TYPE_WORK       = 2
TYPE_MEAL_TIME  = 3
TYPE_NIGHT_WORK = 4
TYPE_RECOVERY   = 5

# Messages d'erreur
#
DB_ERROR_ = "hello"

#  EOF
