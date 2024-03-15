
import string
import random

def str_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# to execute use:
# from randomstr import str_generator
# str_generator()