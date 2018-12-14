
import time
import math
import os
import random
import re
import sys
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    d1_object = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')

    d2_object = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    unixtime_1 = datetime.utcfromtimestamp(time.mktime(d1_object.timetuple()))
    unixtime_2 =datetime.utcfromtimestamp(time.mktime(d2_object.timetuple()))
    print(abs(unixtime_1-unixtime_2))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()
        delta = time_delta(t1, t2)
        # fptr.write(delta + '\n')

    # fptr.close()
