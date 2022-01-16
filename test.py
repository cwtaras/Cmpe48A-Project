import multiprocessing
from multiprocessing import Pool, Value
import os
import time
import requests
from main.helpers.publish_pubsub import make_payment
from main.helpers.insert_to_basket_cloud_func import add_basket

success = 0
fail = 0
  
def worker1():
    returned = make_payment()
    if returned == "OK":
        print("{}-> ok".format(os.getpid()))  
    else:
        print("{}-> not ok".format(os.getpid()))

def worker2():
    returned = add_basket("Headphone")
    if returned.status_code == 200:
        print("{}-> ok".format(os.getpid()))  
    else:
        print("{}-> not ok".format(os.getpid()))
        
if __name__ == "__main__":

    processes1 = []
    for i in range(100):
        processes1.append(multiprocessing.Process(target=worker1))
    pubsub_start = time.time()
    print("---------------Starting PubSub Test--------------")
    for i in range(100):
        processes1[i].start()
    for i in range(100):
        processes1[i].join()
    print("---------------PubSub Test Ended--------------")
    pubsub_end = time.time()

    processes2 = []
    for i in range(100):
        processes2.append(multiprocessing.Process(target=worker2))
    addbasket_start = time.time()
    print("---------------Starting Adding to Baskrt Test--------------")
    for i in range(100):
        processes2[i].start()
    for i in range(100):
        processes2[i].join()
    print("---------------Adding to Basket Test Ended--------------")
    addbasket_end = time.time()


    print("PubSub Completion time -> {}".format(pubsub_end-pubsub_start))
    print("Adding to Basket Test Completion Time -> {}".format(addbasket_end-addbasket_start))
  

   
 