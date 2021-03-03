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
#       This file handles the get requests made to create endpoint         #
###########################################################################

from Util import Structures
from Util import Validation
import docker

def serveCreateEndpoint(requestData):
    response = {}
    if(Validation.ArgumentValidator.validateGetParams(requestData.args, ['ServerName','ServerRAM', 'ServerContainer', 'ServerCPU','ServerDisk'])):
        response = Structures.ObjectMaker.makeBlankSuccessfulResponseObject()
        serverData = Structures.ObjectMaker.makeBlankServerObject()

        serverData['name'] = requestData.args.get('ServerName')
        serverData['ram'] = requestData.args.get('ServerRAM')
        serverData['cpu'] = requestData.args.get('ServerCPU')
        serverData['disk'] = requestData.args.get('ServerDisk')
        serverData['container'] = requestData.args.get('ServerContainer')

        response['result']['dataType'] = 'Server'
        response['result']['serverObject'] = serverData
        try:
            dockerClient = docker.from_env()
        except(FileNotFoundError):
            response = Structures.ObjectMaker.makeErrorResponseObject("Couldn't Communicate with Docker Daemon. Make sure Docker is installed and the Docker Socket is functional.", "502")
            return Structures.JSONReponder.createJSONResponse(response)

        dockerClient.containers.run(serverData['container'], '/bin/sh', detach=True, cpu_shares=10,name=serverData['name'],mem_reservation=serverData['ram'])
    else:
        response = Structures.ObjectMaker.makeErrorResponseObject("Insufficient Arguments Provided", "500")
    return Structures.JSONReponder.createJSONResponse(response)