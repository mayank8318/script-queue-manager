import argparse
import pkgutil
import subprocess
import time
from datetime import datetime
from pathlib import Path

import persistqueue
import os
import logging


resource_package = __name__
resource_path = 'prescripts.txt'


def logStar():
    logging.info('*' * 10)


def logText(header, text):
    logging.info(header + " - BEGIN")
    text = text.split("\n")
    for t in text:
        logging.info(t)
    logging.info(header + " - END")


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
        logging.basicConfig(filename=args.logfile, filemode='a+', level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        while True:
            q = persistqueue.SQLiteQueue(os.path.join(home, 'script_queue'), auto_commit=True)
            if q.size > 0:
                item = q.get()
                CMD = PRE_CMD + "\n" + item
                logStar()
                logText("COMMAND", CMD)
                # print(CMD)
                process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                out, err = process.communicate(CMD.encode('utf-8'))
                logText("OUTPUT", out.decode('utf-8'))
                logStar()
                # print(out.decode('utf-8'))
            time.sleep(args.sleepTime)
            del q

    except Exception as e:
        logging.info("Exception occurred", exc_info=True)
