"""
Instructions for programming Exercise 10.1

Redo the producer/consumer program so that it allows multiple consumers. Each
consumer must be able to consume the same data before the producer produces more
data.

The program should

Print the message Consumer # starting up, where # is the number of the consumer
starting from 0. The producer will set the data as many times as there are
accesses, giving each consumer thread a chance to access the data each time. The
producer should set the data to 1 intially, and then increment it for each
additional access. After each consumer has consumed the data for each access,
print the message Consumer # is done consuming, where # is the number of the
consumer starting from 0. A sample program execution is shown below. Note that
the order of the consumer start ups and accesses may vary with each program
execution.

Enter the number of consumers: 2
Enter the number of accesses: 3
Starting the threads
Producer starting up
Consumer 0 starting up
Consumer 1 starting up
Producer setting data to 1
Consumer 1 accessing data 1
Consumer 0 accessing data 1
Producer setting data to 2
Consumer 0 accessing data 2
Consumer 1 accessing data 2
Producer setting data to 3
Producer is done producing
Consumer 0 accessing data 3
Consumer 0 is done consuming
Consumer 1 accessing data 3
Consumer 1 is done consuming
"""

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
        consumed the data before resetting it."""
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
        """Caller must wait until someone has written the data to access it."""
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

    def __init__(self, cell, accessCount, sleepMax, instance):
        """Create a consumer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name="Consumer" + str(instance))
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
    numConsumers = int(input("Enter the number of consumers: "))

    sleepMax = 4

    cell = SharedCell()
    producer = Producer(cell, accessCount, sleepMax)
    consumerList = []
    for cnt in range(numConsumers):
        consumerList.append(Consumer(cell, accessCount, sleepMax, cnt + 1))

    print("Starting the threads")
    producer.start()
    for consumer in consumerList:
        consumer.start()


if __name__ == '__main__':
    main()
