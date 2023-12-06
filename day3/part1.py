import re
import string

def check_sign(sign):
    if sign not in string.digits and sign != '.':
        return True
    else:
        return False


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    #lines = [s1,s2,s3]
    sums = 0
    reg = r'\d+'
    signs = string.punctuation
    signs = signs.replace('.', '')
    for index, line in enumerate(lines):
        for match in re.finditer(reg, line):
            start = match.span()[0]
            end = match.span()[1]
            checked = False
            if index == 0:
                to_check = ''.join([line[start-1], line[end], lines[index+1][start-1:end+1]])
            elif index == len(lines)-1:
                to_check = ''.join([lines[index - 1][start-1:end+1], line[start-1], line[end]])
            else:
                if start != 0 and end != len(line)-1:
                    to_check = ''.join([lines[index - 1][start-1:end+1], line[start-1], line[end], lines[index+1][start-1:end+1]])
                elif start == 0:
                    to_check = ''.join([lines[index - 1][start:end+1], line[end], lines[index+1][start:end+1]])
                elif end == len(line)-1:
                    to_check = ''.join([lines[index - 1][start-1:end], line[start-1], lines[index+1][start-1:end]])
            for sign in to_check:
                if sign in signs:
                    checked = True
                    sums += int(match.group())
                    break
    print(sums)
        
# CORRECT - 514969 - That one was so shit...
        
if __name__ == '__main__':
    main()