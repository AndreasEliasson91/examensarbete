from functions import lists as l
import random


if __name__ == '__main__':
    # time1 = l.comprehension(100_000_000)
    # time2 = l.append([x for x in range(100_000_000)])
    # print('Comp:', time1)
    # print('App:', time2)
    time = l.sort([random.choice(1000) for _ in range(100_000)])
