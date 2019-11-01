import threading
import time
import Queue

def subscriber_function(queue_object):
  while not queue_object.empty():
    item = queue_object.get()
    if item is None:
      break
    print("{} removed {} from the queue \n".format(threading.current_thread(), item))
    queue_object.task_done()


# Create an LifoQueue object
queue_object = Queue.Queue()
# Populate the queue
for i in range(10):# 0-9
  queue_object.put(i)

thread_1 = threading.Thread(target=subscriber_function, args=(queue_object,), name="Thread One")
thread_2 = threading.Thread(target=subscriber_function, args=(queue_object,), name="Thread Two")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

# for thread_ in threads:
#   print "wait until {} was executed completely".format(thread_)
#   thread_.join()

print queue_object
print "Queue is empty"
