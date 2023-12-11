import re
import string
from functools import reduce


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    for index, line in enumerate(lines):
        for match in re.finditer(r'\*', line):
            start = match.span()[0]
            end = match.span()[1]
            before = lines[index-1][start-1:end+1]
            inline = lines[index][start-1:end+1]
            after = lines[index+1][start-1:end+1]
            gear_counter = 0
            to_check = [before,inline,after]
            to_find = []
            temp = []
            for line_index, checked in enumerate(to_check, start=-1):
                found_in_line = False
                for position, sign in enumerate(checked, start=start):
                    if sign in string.digits:
                        if not found_in_line:
                            found_in_line = True
                            gear_counter += 1
                            temp.append((line_index, position))
                        elif re.match(r'\d\.\d', checked) or '*' in checked:
                            gear_counter += 1
                            temp.append((line_index, position))
            print(gear_counter)
            if gear_counter == 2:
                for pair in temp:
                    to_find.append(pair)
                    #print(pair)
            nums = []
            #print(to_find)
            for pair in to_find:
                print(pair)
                for number_match in re.finditer(r'\d+', lines[index+pair[0]]):
                    if pair[1] >= number_match.start() and pair[1] <= number_match.end():
                        nums.append(int(number_match.group()))
                        print(number_match.group())
            #if len(nums) != 0:
                #print(nums)
            if len(nums) != 0:
                sums += reduce(lambda x,y : x*y, nums, 1)
                print('-----------')
        #
    print(sums)

            
if __name__ == '__main__':
    main()
    
    