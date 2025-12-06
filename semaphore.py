import threading
import time

sema = threading.Semaphore(3)

def worker(id):
    print(f"Worker {id} waiting...")
    with sema:
        print(f"Worker {id} entered critical section")
        time.sleep(1)
    print(f"Worker {id} finished")

threads = []

for i in range(6):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
