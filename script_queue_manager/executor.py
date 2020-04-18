import argparse
import pkgutil
import time
from datetime import datetime
from pathlib import Path

import persistqueue
import os

resource_package = __name__
resource_path = 'prescripts.txt'


def executor():
    home = os.path.join(str(Path.home()), 'sqm')
    if not os.path.exists(home):
        os.makedirs(home)

    parser = argparse.ArgumentParser(prog='executor',
                                     description='Execute script tasks from the queue')
    parser.add_argument('-p', '--pre_script', action='store', dest='prescript', default=None)
    parser.add_argument('-l', '--log_file', action='store', dest='logfile', default=os.path.join(home, 'logs.txt'))
    parser.add_argument('-s', '--sleep_time', action='store', dest='sleepTime', default=15, type=int)
    args = parser.parse_args()

    prescriptFile = args.prescript

    if not prescriptFile:
        prescriptFile = './prescripts.txt'
        file = pkgutil.get_data(__name__, prescriptFile).decode()
        PRE_CMD = file
    else:
        file = open(prescriptFile, 'r')
        PRE_CMD = ''
        for l in file:
            PRE_CMD += l

    try:
        while True:
            q = persistqueue.SQLiteQueue(os.path.join(home, 'script_queue'), auto_commit=True)
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
        logFile = open(args.logfile, 'a+')
        logFile.write("Error occurred!!!!")
        logFile.write(e)
