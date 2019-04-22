"""
Reader - Writer thread sync
"""

import time, random
from threading import Thread, currentThread, Condition


class Counter(object):
    """Defines a counter object and supporting methods"""

    def __init__(self, startAt):
        self.count = int(startAt)
        print("Counter init: counter = " + str(self.count))

    def __str__(self):
        str(self.count)

    def increment(self):
        self.count += 1
        print("Incremented counter to " + str(self.count))
        return self.count

    def decrement(self):
        self.count -= 1
        print("Decremented counter to " + str(self.count))
        return self.count


class SharedCell(object):
    """Synchronizes readers and writers around shared data,
    to support thread-safe reading and writing."""

    def __init__(self, data):
        """Sets up the conditions and the count of
        active readers."""
        self.data = data
        self.writing = False
        self.readerCount = 0
        self.okToRead = Condition()
        self.okToWrite = Condition()

    def __str__(self):
        str(self.data)

    def read(self, readerFunction):
        """Observe the data in the shared cell."""
        self.beginRead()
        # Enter the reader's critical section
        result = readerFunction(self.data)
        # Exit the reader's critical section
        self.endRead()
        return result

    def write(self, writerFunction):
        """Observe the data in the shared cell."""
        self.beginWrite()
        # Enter the writer's critical section
        result = writerFunction(self.data)
        # Exit the writer's critical section
        self.endWrite()
        return result

    def beginRead(self):
        """Waits until a writer is not writing or the writers
        condition queue is empty. Then increments the reader
        count and notifies the next waiting reader."""
        self.okToRead.acquire()
        self.okToWrite.acquire()
        while self.writing or len(self.okToWrite._waiters) > 0:
            self.okToRead.wait()
        self.readerCount += 1
        self.okToRead.notify()

    def endRead(self):
        """Notifies a wating writer if there are
        no active readers."""
        self.readerCount -= 1
        if self.readerCount == 0:
            self.okToWrite.notify()
        self.okToWrite.release()
        self.okToRead.release()

    def beginWrite(self):
        """Can only write when someone else is not
        writing and there are no readers ready."""
        self.okToWrite.acquire()
        self.okToRead.acquire()
        while self.writing or self.readerCount != 0:
            self.okToWrite.wait()
        self.writing = True

    def endWrite(self):
        """Notify the next wating writer if the readers
        condition queue is empty. Otherwise, notify the
        next waiting reader."""
        self.writing = False
        if len(self.okToRead._waiters) > 0:
            self.okToRead.notify()
        else:
            self.okToWrite.notify()
        self.okToRead.release()
        self.okToWrite.release()


class Reader(Thread):
    """Reads from the shared cell"""

    def __init__(self, cell, accessCount, sleepMax, instance):
        """Create a reader of the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name="Reader" + str(instance))
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
            value = self.cell.read(lambda counter: self.cell.data.count)
            print("%s is done getting %s" % (self.getName(), str(value)))


class Writer(Thread):
    """Increments the value in the shared cell"""

    def __init__(self, cell, accessCount, sleepMax, instance):
        """Create a writer to the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name="Writer" + str(instance))
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
            value = self.cell.write(lambda counter: counter.increment())
            print("%s is done incrementing to %s" % (self.getName(), str(value)))


def main():
    """Get the number of accesses from the user, create a
    shared cell, and create and start up the specified number
    of writers and readers."""
    accessCount = int(input("Enter the number of accesses: "))
    numWriters = int(input("Enter the number of writers: "))
    numReaders = int(input("Enter the number of readers: "))

    sleepMax = 4

    counter = Counter(0)
    print("counter defined at:", str(counter.count))
    cell = SharedCell(counter)
    print("shared counter data:", str(cell.data.count))

    writerList = []
    readerList = []
    for cnt in range(numWriters):
        writerList.append(Writer(cell, accessCount, sleepMax, cnt + 1))
    for cnt in range(numReaders):
        readerList.append(Reader(cell, accessCount, sleepMax, cnt + 1))

    print("Starting the threads")
    for writer in writerList:
        writer.start()
    for reader in readerList:
        reader.start()


if __name__ == '__main__':
    main()
