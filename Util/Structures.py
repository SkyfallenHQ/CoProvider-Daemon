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
#                This file helps create json responses                     #
###########################################################################

import json

class JSONReponder:

    @staticmethod
    def createJSONResponse(fromDict):
        return json.dumps(fromDict)

class ObjectMaker:

    @staticmethod
    def makeBlankSuccessfulResponseObject():
        newR = {

            "status": {
                "code": 200,
                "message": "Successful Request",
                "error": False
            },
            "result": {

                "dataType": False

            }

        }
        return newR

    @staticmethod
    def makeErrorResponseObject(errorMsg, errorCode):
        newR = {

            "status": {
                "code": errorCode,
                "message": "Failed Request (Errored out)",
                "error": errorMsg
            },
            "result": {

                "dataType": False

            }

        }
        return newR

    @staticmethod
    def makeBlankServerObject():
        newSR = {

            "name": "",
            "ram": 0,
            "cpu": 0,
            "disk": 0,
            "container": "alpine",
            "status": "stopped"

        }
        return newSR