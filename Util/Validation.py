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
#                  This file helps validate requests                       #
###########################################################################

class ArgumentValidator:

    def validateGetParams(requestArgs, paramsToValidate):

        for x in paramsToValidate:

            y = requestArgs.get(x)
            if(y == "" or y == None):
                return False

        return True