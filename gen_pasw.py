import string
import secrets as sec
from random import shuffle
from random import randint
from math import trunc


def gen(n):
    symb = randint(1, 2)
    lower = trunc(n * 0.3)
    upper = trunc(n * 0.3)
    digit = n - lower - upper - symb
    gen_lower_char = [sec.choice(string.ascii_lowercase) for _ in range(lower)]
    gen_upper_char = [sec.choice(string.ascii_uppercase) for _ in range(upper)]
    gen_digits = [sec.choice(string.digits) for _ in range(digit)]
    gen_symbol = [sec.choice('/_$&') for _ in range(symb)]
    gen_password = [*gen_lower_char, *gen_upper_char, *gen_digits, *gen_symbol]
    shuffle(gen_password)
    password = ''.join(gen_password)
    for _ in ('/_$&'):
        if password[0] == _:
            pas = list(password)
            pas[0] = sec.choice(string.ascii_uppercase)
            password = ''.join(pas)
    return(password)
