import re
from collections import Counter
from functools import reduce

mapping = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    max_rank = len(lines)
    with_wages = {}
    for index,line in enumerate(lines):
        hand, bid = line.split(' ')
        wild_power = []
        count = {char: line.count(char) for char in line}
        print(count)
        #for idx, sign in enumerate(hand):
            


if __name__ == "__main__":
    main()