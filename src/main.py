import cProfile, pstats
import getopt
import logging
import platform
import sys

from datetime import datetime


 # TODO: Fix import of cython implementation
 
# from cython_test_cases import cython_run
from functions import dicts
from functions import generators
from functions import iterator
from functions import lists
from functions import sets
from functions import tuples


VERSION = platform.python_version()
PROFILING = False

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.INFO,
    filename='c:/code/projects/master-thesis/doc/logs/test_cases.log'
    # filename='c:/code/projects/master-thesis/doc/logs/log_book.log'
)


# def main(argv: list) -> None:
def main(argv):
    if len(argv) < 1:
        logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logging.warning('Couldn\'t run MAIN(). Not enough CL parameters\n')
        # help_msg = '''ERROR: Missing params to run MAIN(), add any of following params:\n
        # -d | --dict: Run dictionary functions
        # -g | --generator: Run generator functions
        # -i | --iter: Run iteration functions
        # -l | --list: Run list functions
        # -s | --set: Run set functions
        # -t | --tuple: Run tuple functions
        # '''
        # print(help_msg)
        return
    
    try:
        options, _ = getopt.getopt(argv, 'dgilstc:p:r:', ['cython', 'dict', 'generator', 'iter', 'list', 'set', 'tuple'])

    except getopt.GetoptError:
        logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logging.warning('Option: %s doesn\'t exist\n', str(argv))
        # help_msg = f'''ERROR: Option {str(argv)} doesn\'t exist, try any of following options:\n
        # -d | --dict: Run dictionary functions
        # -g | --generator: Run generator functions
        # -i | --iter: Run iteration functions
        # -l | --list: Run list functions
        # -s | --set: Run set functions
        # -t | --tuple: Run tuple functions
        # '''
        # print(help_msg)
        sys.exit(2)

    for opt, _ in options:
        if opt in ['-d', '--dict']:
            dicts.run(VERSION)
        elif opt in ['-g', '--generator']:
            generators.run(VERSION)
        elif opt in ['-i', '--iter']:
            iterator.run(VERSION)
        elif opt in ['-l', '--list']:
            lists.run(VERSION)
        elif opt in ['-s', '--set']:
            sets.run(VERSION)
        elif opt in ['-t', '--tuple']:
            tuples.run(VERSION)
#         # elif opt == '-c':
#              # from cpp import cpp
#              # cpp.run()
        # elif opt == '--cython':
        #     cython_run()
        

if __name__ == '__main__':
    # if PROFILING:
    #     filename = '-'.join(VERSION.split('.'))

    #     profiler = cProfile.Profile()
    #     profiler.enable()

    #     main(sys.argv[1:])

    #     profiler.disable()

    #     stats = pstats.Stats(profiler).sort_stats('cumtime')
    #     stats.strip_dirs()

    #     stats.print_stats()
    #     stats.dump_stats('C:/code/projects/master-thesis/doc/results/cprofile/{0}.txt'.format(filename))
    # else:
    main(sys.argv[1:])
