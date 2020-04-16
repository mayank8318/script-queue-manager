import argparse
import pkgutil
import time
from datetime import datetime

import persistqueue

resource_package = __name__
resource_path = 'prescripts.txt'


def executor():
    parser = argparse.ArgumentParser(prog='executor',
                                     description='Execute script tasks from the queue')
    parser.add_argument('-p', '--pre_script', action='store', dest='prescript', default='./prescripts.txt')
    parser.add_argument('-l', '--log_file', action='store', dest='logfile', default='./logs.txt')
    parser.add_argument('-s', '--sleep_time', action='store', dest='sleepTime', default=15, type=int)
    args = parser.parse_args()

    prescriptFile = args.prescript
    file = pkgutil.get_data(__name__, "prescripts.txt").decode()

    PRE_CMD = file

    # for l in file:
    #     print(l)
    #     PRE_CMD += l + '\n'

    # file.close()

    try:
        while True:
            q = persistqueue.SQLiteQueue('script_queue', auto_commit=True)
            if q.size > 0:
                item = q.get()
                CMD = PRE_CMD + item
                print(CMD)
                STAMP = datetime.now()
                logFile = open(args.logfile, 'a+')
                logFile.write(str(STAMP) + '\t' + CMD)
                logFile.close()
            time.sleep(args.sleepTime)
            del q

    except Exception as e:
        logFile.write("Error occurred!!!!")
        logFile.write(e)
        print(e)
