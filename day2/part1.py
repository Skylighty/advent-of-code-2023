import re 

VALS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    for index,line in enumerate(lines, start=1):
        matches = re.findall(r'(\d+) ([a-z]+)', line)
        sums += index
        for match in matches:
            if match[1] in VALS.keys():
                if int(match[0]) > VALS[match[1]]:
                    sums -= index
                    break
    print(sums)

# CORRECT - 2105

if __name__ == '__main__':
    main()