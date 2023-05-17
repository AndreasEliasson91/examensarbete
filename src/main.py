import cProfile, pstats
import getopt
import logging
import platform
import sys

from datetime import datetime

from cython_test_cases import run_cython
from functions import dicts, generators, iterator, lists, sets, tuples


VERSION = platform.python_version()
LOG_DIR = '../doc/logs/'
LOG_FILE = 'test_cases.log'
PROFILING = False

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.INFO,
    filename=LOG_DIR + LOG_FILE
    # filename='c:/code/projects/master-thesis/doc/logs/log_book.log'
)

        
def profiling(profiling_dir, profiling_file):
    profiler = cProfile.Profile()
    profiler.enable()

    main(sys.argv[1:])

    profiler.disable()

    with open(profiling_dir + profiling_file, 'w', encoding='utf-8') as out_file:
        stats = pstats.Stats(profiler, stream=out_file).sort_stats('cumtime')
        stats.strip_dirs()
        stats.print_stats()

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
        elif opt == '--cython':
            run_cython()

if __name__ == '__main__':
    main(sys.argv[1:])
