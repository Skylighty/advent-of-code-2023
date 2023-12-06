


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    for index, line in enumerate(lines):
        winning, mine = line.split('|')
        bullshit, winning = winning.split(':')
        winning_split = winning.split(' ')
        mine_split = mine.split(' ')
        mine_split[len(mine_split)-1] = mine_split[len(mine_split)-1].replace('\n', '')
        for item in mine_split:
            item.strip()
            if item == '':
                mine_split.remove(item)
        for item in winning_split:
            item.strip()
            if item == '':
                winning_split.remove(item)
        print(winning_split)
        print(mine_split)
        temp_points = 0
        for item in winning_split:
            if item in mine_split:
                if temp_points == 0:
                    temp_points = 1
                else:
                    temp_points *= 2
        sums += temp_points
    print(sums)
    
# CORRECT - 21213
        
if __name__ == '__main__':
    main()