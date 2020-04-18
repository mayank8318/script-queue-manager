import argparse
import os
from pathlib import Path

import persistqueue


def pusher():
    home = os.path.join(str(Path.home()), 'sqm')
    if not os.path.exists(home):
        os.makedirs(home)

    parser = argparse.ArgumentParser(prog='pusher',
                                     description='Push script tasks to the queue')
    parser.add_argument('-s', '--script', required=True, action='store', dest='script')
    args = parser.parse_args()

    script = args.script

    try:
        q = persistqueue.SQLiteQueue(os.path.join(home, 'script_queue'), auto_commit=True)
        q.put(script)

        print("Script added successfully")
    except Exception as e:
        print("Error occurred!!!!")
        print(e)


