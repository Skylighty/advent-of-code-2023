import re

MAPPING = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    for line in lines:
        mapped = {}
        for index, sign in enumerate(line):
            if sign.isdigit():
                mapped[index] = sign
        for text_number in MAPPING.keys():
            if text_number in line:
                indices = [match.start() for match in re.finditer(text_number, line)] 
                for indice in indices:
                    mapped[indice] = MAPPING[text_number]
        sorted_map = sorted(mapped.items(), key=lambda x: x[0])
        first = sorted_map[0][1] 
        last = sorted_map[-1][1]
        sums += int(f'{first}{last}')
    print(sums)

# CORRECT - between 54076 and 54090

if __name__ == "__main__":
    main()