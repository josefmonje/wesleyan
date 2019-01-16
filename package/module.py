__all__ = [
    'ask_ok',
    'divide',
    'incrementer',
]

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def my_function(*args, **kwargs):
    print(args, kwargs)


def divide(x, y):
    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print("division by zero!")
    except (ValueError, KeyboardInterrupt):
        print("numbers only!")
    except Exception as err:
        print("New error occurred: ", err)
    else:
        print("result is", result)
    finally:
        print("finally!")


def incrementer(n):
    return n + 1