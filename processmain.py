#  ____  _           __       _ _            #
# / ___|| | ___   _ / _| __ _| | | ___ _ __  #
# \___ \| |/ / | | | |_ / _` | | |/ _ \ '_ \ #
#  ___) |   <| |_| |  _| (_| | | |  __/ | | |#
# |____/|_|\_\\__, |_|  \__,_|_|_|\___|_| |_|#
#             |___/                          #########
#   ____      ____                 _     _           #
#  / ___|___ |  _ \ _ __ _____   _(_) __| | ___ _ __ #
# | |   / _ \| |_) | '__/ _ \ \ / / |/ _` |/ _ \ '__|#
# | |__| (_) |  __/| | | (_) \ V /| | (_| |  __/ |   #
#  \____\___/|_|   |_|  \___/ \_/ |_|\__,_|\___|_|   #
#                                                    #
###########################################################################
#                   (C) 2021 - Skyfallen Developers                       #
#                      Skyfallen CoProvider Beta                          #
#            Manage your containerized servers with ease.                 #
#                        ----DAEMON CODE----                              #
#                     This file runs everything                            #
###########################################################################

import flask
from Endpoints import Root
import sqlite3
from os import path
from DB import Initiator

class CoProviderFramework:
    def HandleDaemon(self):

        app = flask.Flask(__name__)

        dbNeedsInit = False

        if (path.exists('CPFD_DB.db') == False):
            dbNeedsInit = True

        conn = sqlite3.connect('CPFD_DB.db')

        if(dbNeedsInit):
            Initiator.SQLInitiator.createTables(conn)

        @app.errorhandler(404)
        def route404(e):
            return Root.APIEndpoint.serveNotFound()

        @app.route('/createServer/')
        def RouteCreateServer():
            return Root.APIEndpoint.serveCreate(flask.request)


        app.run()