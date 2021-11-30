import queue
import socket
from multiprocessing import Process, Queue
import threading

q = Queue()
q.put("hello")
print(q.get())
print(q.get())

