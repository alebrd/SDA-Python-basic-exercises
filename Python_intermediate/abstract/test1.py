import time

class Timed0peration:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, val, traceback):
        time_spent = time.time() - self.start
        print(f'Time spent :: {time_spent}')

with Timed0peration() as val:
    print(val)
    print("Heavy calculation")
    time.sleep(1)