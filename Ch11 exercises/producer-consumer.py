

import time, random
from threading import Thread, currentThread, Condition


class SharedCell(object):
    """Shared data for the producer / consumer problem."""

    def __init__(self):
        """Data undefined at startup."""
        self.data = -1
        self.writeable = True
        self.condition = Condition()

    def block_thread_on(self, block_condition):
        self.condition.acquire()
        while block_condition:
            self.condition.wait()

    def release_thread_lock(self):
        self.condition.notify()
        self.condition.release()

    def setData(self, data):
        """Second caller must wait until someone has
        consumed the data before restting it."""
        # block_condition = not self.writeable
        # self.block_thread_on(block_condition)
        self.condition.acquire()
        # while block_condition:
        while not self.writeable:
            self.condition.wait()
        print("%s setting data to %d" % \
              (currentThread().getName(), data))
        self.data = data
        self.writeable = False
        self.release_thread_lock()

    def getData(self):
        """Caller must wait until someon has written the data to access it."""
        # block_condition = self.writeable
        # self.block_thread_on(block_condition)
        self.condition.acquire()
        # while block_condition:
        while self.writeable:
            self.condition.wait()
        print("%s accessing data %d" % \
              (currentThread().getName(), self.data))
        self.writeable = True
        self.release_thread_lock()
        return self.data


class Producer(Thread):
    """A producer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name="Producer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        """Announce start-up, sleep and write to shared 
        cell the given number of times, and announce
        completion."""
        print("%s starting up" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            self.cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())


class Consumer(Thread):
    """A consumer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a consumer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name="Consumer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        """Announce start-up, sleep and read from shared
        cell the given number of times, and announce
        completion."""
        print("%s starting up" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            value = self.cell.getData()
        print("%s is done consuming\n" % self.getName())


def main():
    """Get the number of accesses from the user, create a
    shared cell, and create and start up a producer and a
    consumer."""
    accessCount = int(input("Enter the number of accesses: "))
    sleepMax = 4
    cell = SharedCell()
    producer = Producer(cell, accessCount, sleepMax)
    consumer = Consumer(cell, accessCount, sleepMax)
    print("Starting the threads")
    producer.start()
    consumer.start()


if __name__ == '__main__':
    main()
