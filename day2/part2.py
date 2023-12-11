from functools import reduce
import re


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    for line in lines:
        colours = {
            'red': [],
            'green': [], 
            'blue': []
        }
        matches = re.findall(r'(\d+) ([a-z]+)', line)
        for match in matches:
            for colour in colours:
                if colour in match[1]:
                    colours[colour].append(int(match[0]))
        powers = [max(values) for values in colours.values()]
        multiplied = reduce(lambda x,y : x*y, powers, 1)
        sums += multiplied
    print(sums)

# CORRECT

if __name__ == '__main__':
    main()