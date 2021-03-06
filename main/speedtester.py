import json
import os
from subprocess import call
import subprocess
import datetime
from iftt_webhooks import do_email
from key import iftt_metrics_key

__author__ = 'charlie'

date_time_format = "%Y-%m-%d_%H_%M_%S"
speedtest_file_loc = "%s/logs/speedtest" % os.getenv("HOME")

def speedtester():
    print("Running speedtest")
    filename = get_speedtest_file_name()
    cmd = "speedtest --simple --share > %s" % get_speedtest_file_name()
    print("Checking to see if %s exists" % speedtest_file_loc)
    if not os.path.exists(speedtest_file_loc):
        print("Creating directory structure at %s" % speedtest_file_loc)
        make_directories()
    print("Running speedtest and pushing results to %s" % filename)
    os.system(cmd)
    print("Log published at %s" % filename)
    email_results(filename)


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


def email_results(filename):
    f = open(filename, "r")
    data = f.readlines()
    data_string = ""
    for line in data:
        data_string += "%s\n" % line
    f.close()
    print("Emailing results.")
    payload = {'value1': 'Daily Speedtest Results', 'value2': data_string, 'value3': ''}
    print(do_email(iftt_metrics_key, "metrics", payload))


if __name__ == "__main__":
    speedtester()