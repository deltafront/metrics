import os
from subprocess import call
import subprocess
import datetime

__author__ = 'charlie'

date_time_format = "%Y-%m-%d'T'%H:%M:%S"
speedtest_file_loc = "%s/logs/speedtest" % os.getenv("HOME")

def speedtester():
    print("Running speedtest")
    cmd = "speedtest --simple --share"
    print("Checking to see if %s exists" % speedtest_file_loc)
    if not os.path.exists(speedtest_file_loc):
        print("Creating directory structure at %s" % speedtest_file_loc)
        make_directories()
    filename = get_speedtest_file_name()
    print("Running speedtest and pushing results to %s" % filename)
    logfile = open(filename,"w")
    p = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=logfile)
    ret_code = p.wait()
    logfile.flush()
    logfile.close()
    print(ret_code)
    print("Log published at %s" % filename)



def get_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime(date_time_format)
    return timestamp

def get_speedtest_file_name():
    return "%s/%s.speedtest.log" % (speedtest_file_loc, get_timestamp())


def make_directories():
    print("Making directories.")
    home = os.getenv("HOME")
    logs_loc = "%s/logs" % home
    make_dir(logs_loc)
    speedtest_logs_loc = "%s/speedtest" % logs_loc
    make_dir(speedtest_logs_loc)

def make_dir(directory):
    print("Checking to see if directory %s exists" % directory)
    if not os.path.exists(directory):
        print("Making directory %s" % directory)
        os.mkdir(directory)



if __name__ == "__main__":
    speedtester()