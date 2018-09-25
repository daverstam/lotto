#!/usr/bin/env python3

import random
import argparse

def random_number():
    """ lotto is in the range 1-35 """
    return str(random.randrange(1, 36))

def random_joker_number():
    """ optional joker is in the range 0-9 """
    return str(random.randrange(0, 9))

def main():
    descstr = """ Randomizer for Swedish Lotto (https://www.svenskaspel.se/lotto) """
    parser = argparse.ArgumentParser(description=descstr)
    parser.add_argument('-j', '--joker', dest = 'joker', action = 'store_true', help = 'Also randomizes a seven-digit joker number', required = False)
    args = parser.parse_args()

    if args.joker:
        print('Lotto row:')
        """ lotto and joker is 7 digits """
        print(', '.join([random_number() for n in range(0 ,7)]))
        print('---' * len(range(0, 7)))
        print('Joker row:')
        print(', '.join([random_joker_number() for n in range(0, 7)]))
    else:
        print('Lotto row:')
        print(', '.join([random_number() for n in range(0, 7)]))

if __name__ == '__main__':
    main()
