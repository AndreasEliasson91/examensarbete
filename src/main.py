from functions import lists as l
from functions import tuples as t
from functions import dicts as d
from functions import generators as g
import random


if __name__ == '__main__':
    # time1 = l.comprehension(100_000_000)
    # time2 = l.append([x for x in range(100_000_000)])
    # print('Comp:', time1)
    # print('App:', time2)
    # time = l.sort([random.choice(1000) for _ in range(100_000)])
    # time = t.tuple_append([x for x in range(100_000)])
    # time = t.tuple_sort(tuple([random.choice(range(10_000)) for _ in range(10)]))

    # time = d.dictionary_comprehension([x for x in range(100_000)], [x for x in range(100_000)])
    # time = d.dictionary_insert([x for x in range(10_000_000)], [x for x in range(10_000_000)])
    time = g.generator_iter([x for x in range(10_000_000)])
