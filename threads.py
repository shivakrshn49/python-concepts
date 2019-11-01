# Process - A main program with huge bunch of lines of code like python interpretter which runs python code, running any python file with some python
#           code in it can be said to a process
# Sub Process (Thread) - A thread is also called as sub process i.e., splitting a big task(process) in to sub tasks(sub processes/threads)

################################################## import threading ####################################

import threading
import time


# class based

threadLock = threading.Lock()

class LeargningThread(threading.Thread):
   global_counter = 0

   def __init__(self, threadID, name, delay, type_):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.type_ = type_

   def run(self):
      threadLock.acquire()
      print ("Starting the thread --> " + self.name)
      print_time(self.name, self.delay, 5, self.type_)
      print ("Exiting " + self.name)
      threadLock.release()
      


def print_time(threadName, delay, counter, type_):
   print "The initial loop count for '{0}' is '{1}', i.e., {2}".format(type_, counter, ', '.join(map(str, range(1,counter+1))))
   while counter:
      print "picked up '{}' from loop for '{}'".format(counter, type_), threadName, "<-------- thread name"
      time.sleep(delay)
      if type_ == 'add':
        print "--------> Adding counter '{0}' + LeargningThread.global_counter '{1}'".format(counter, LeargningThread.global_counter)
        LeargningThread.global_counter = LeargningThread.global_counter + counter
        print "--------> Addition Result is '{}'".format(LeargningThread.global_counter)
      else:
        print "--------> substracting counter '{0}' - LeargningThread.global_counter '{1}'".format(counter, LeargningThread.global_counter)
        LeargningThread.global_counter = LeargningThread.global_counter - counter
        print "--------> substraction Result is '{}'".format(LeargningThread.global_counter)
      # print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1
   print "Total Count for thread {} is {}".format(threadName, LeargningThread.global_counter)

# Create new threads
thread1 = LeargningThread(1, "Thread-1", 1, 'add')
thread2 = LeargningThread(2, "Thread-2", 2, 'substract')

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")


