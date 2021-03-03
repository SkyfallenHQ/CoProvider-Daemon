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
#                This file creates the database structure                  #
###########################################################################

class SQLInitiator:

    @staticmethod
    def createTables(conn):

        c = conn.cursor()
        c.execute('''CREATE TABLE authkeys (client_id text, client_secret text, client_name text)''')

        conn.commit()