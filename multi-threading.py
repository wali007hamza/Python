import sys
import datetime
import time
from asyncio import Lock
from multiprocessing.dummy import Pool as ThreadPool


class Lease:
    def __init__(self, time: datetime):
        self.start_time = time


def function(dto: tuple()):
    while(True):
        print("Hi_" + str(dto[1]))
        try:
            if ((datetime.datetime.utcnow() - dto[0].start_time).total_seconds() > 10):
                raise "Time expired, renew lease"
        except Exception as ex:
            dto[2].acquire()
            if ((datetime.datetime.utcnow() - dto[0].start_time).total_seconds() > 10):
                print('Catching exception')
                dto[0].start_time = datetime.datetime.utcnow()

        time.sleep(1)


if __name__ == "__main__":
    lease_object = Lease(datetime.datetime.utcnow())
    # number_of_threads = int(input().strip())
    degree_of_parallelism = 5
    threads = ThreadPool(degree_of_parallelism)
    lock = Lock()
    results = threads.map(function, [(lease_object, i, lock)
                                     for i in range(degree_of_parallelism)])
    threads.close()
    threads.join()
