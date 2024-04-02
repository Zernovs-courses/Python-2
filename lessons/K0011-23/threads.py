import logging
import threading
import time


def thread_fun(name):
    logging.info(f"Thread {name}: starting")

    time.sleep(2)

    logging.info(f"Thread {name}: finishing")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main : before creating thread")

    x = threading.Thread(target=thread_fun, args=(1,), daemon=True)

    logging.info("Main : before running thread")

    x.start()
    
    logging.info("Main : wait for thread to finish")

    logging.info("Main : all done")