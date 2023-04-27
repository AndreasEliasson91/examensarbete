import time


class Timer():
    def __init__(self) -> None:
        self.start = time.time()
        self.runtime = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.runtime = round(end - self.start, 2)

        print(f'The function took {self.runtime} seconds')
        return self.runtime


def test_run() -> None:
    import random

    for _ in range(10):
        time.sleep(random.choice(range(1,5)))


if __name__ == '__main__':
    t = Timer()
    with t:
        test_run()

    time = t.runtime
    print(time)

     