import getopt
import logging
import random
import sys
from datetime import datetime

from functions import lists as l
from functions import tuples as t

from functions import generators as g
from functions import iterator as i

from data import generate_data

VERSION = str(sys.version)

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.INFO,
    filename='./doc/logs/log_book.log'
)


# def main(argv: list) -> None:
#     if len(argv) < 1:
#         logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#         logging.warning('Not enough parameters')
#         return
    
#     try:
#         options, args = getopt.getopt(argv, 'dgilt:c:p:r:', ['cython', 'dict', 'generator', 'iter', 'list', 'tuple'])
#     except getopt.GetoptError:
#         logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#         logging.warning('Option doesn\'t exist')
#         sys.exit(2)

#     for opt, arg in options:
#         if opt in ['-d', '--dict']:
#             from functions import dicts
#             dicts.run()
#         elif opt in ['-g', '--generator']:
#             from functions import generators
#             generators.run()
#         elif opt in ['-d', '--dict']:
#             from functions import dicts
#             dicts.run()
#         elif opt in ['-i', '--iter']:
#             from functions import iterator
#             iterator.run()
#         elif opt in ['-l', '--list']:
#             from functions import lists
#             lists.run()
#         # elif opt == '-c':
#              # from cpp import cpp
#              # cpp.run()
#         # elif opt == 'cython':
#         #     from functions import dicts
#         #     dicts.run()
        # elif opt == '-p':
        #     from functions import dicts
        #     dicts.run() PROFILER RUN
            # elif opt == '-r':
            #     reload_data = True
        

if __name__ == '__main__':
    # time1 = l.list_comprehension(1_000_000)
    # time2 = l.list_append([x for x in range(1_000_000)])
    # # print('Comp:', time1)
    # # print('App:', time2)
    # # time = l.list_sort([random.choice(1000) for _ in range(100_000)])
    # time = t.tuple_append([x for x in range(100_000)])
    # time = t.tuple_sort(tuple([random.choice(range(10_000)) for _ in range(10)]))

    # time = d.dictionary_comprehension([x for x in range(100_000)], [x for x in range(100_000)])
    # time = d.dictionary_insert([x for x in range(1_000_000)], [x for x in range(1_000_000)])
    # time = g.generator_iter([x for x in range(1_000_000)])

    # # first_name = ''
    # # last_name = ''
    # # argv = sys.argv[1:]

    # # try:
    # #     opts, args = getopt.getopt(argv, 'f:l:', ['first_name =', 'last_name ='])
    # # except:
    # #     print('Error')

    # # for opt, arg in opts:
    # #     print(opt)
    # #     if opt in ['-f', '--first_name']:
    # #         first_name = arg
    # #     elif opt in ['-l', '--last_name']:
    # #         last_name = arg
        
    # # print(first_name + ' ' + last_name)
    # # print(VERSION)
    # time = i.iteration_test(set(range(1_000_000)))
    # time = i.iteration_test(list(range(1_000_000)))
    # time = i.iteration_test(tuple(range(1_000_000)))
    
    generate_data.generate_dict_keys(10, reload=reload_data)