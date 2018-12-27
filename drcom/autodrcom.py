#!/bin/python2.7
# Script to check connection status.
# While connection is closed, run [redrcom]
# Created by Ekira
# 2017/7/20
# Modified 2017/10/3

import os, time
from subprocess import Popen, PIPE


CONN_RETRY      = 10
CHECK_TIMEOUT   = 30
RESTART_DRCOM   = "redrcom.sh"
LOG_PATH        = "~/autodrcom.log"


def log(text):
    try:
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_PATH, "at") as f:
            f.write(now + "  " + text + "\n")
    except:
        pass


def main():
    retry = 0
    while True:
        cmd = "ping 114.114.114.114 -c 2"
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        out = p.stdout.read()
        err = p.stderr.read()
        if len(out)  == 0 or len(err) > 0:
            log(err)
            break
        if "0 received" in out.replace("\n", ""):
            if retry == CONN_RETRY:
                log("Connection Error, EXIT, retry=%d" % retry)
                break
            log("Connection Error, run [redrcom], retry=%d" % retry)
            os.system(RESTART_DRCOM)
            retry += 1
        else:
            retry = 0
        time.sleep(CHECK_TIMEOUT)


if __name__ == "__main__":
    main()
