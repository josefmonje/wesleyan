import package

from package.subpackage.other_module import hello_world
from package.subpackage.other_module import hello_world as hw

# from package.module import my_function, divide, incrementer
# from package.module import *

if __name__ == '__main__':
    print(__name__)
    print('Welcome to my script!')

    hello_world()

    package.module.ask_ok('Is it ok?')
    # my_function()
    package.module.ask_ok('Final answer?')

