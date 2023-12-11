import queue

def evaluate_card(winning_card, mine_card, index):
    counter = 0 
    for winning_number in winning_card:
        if winning_number in mine_card:
            counter += 1
    if counter > 0:
        return (index, coutner)
    else:
        return None



def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    formatted_lines = []
    que = queue.Queue()
    for index,line in enumerate(lines):
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
        formatted_lines.append((winning_split, mine_split))
    for index, line in enumerate(formatted_lines, start=1):
        for full_card in formatted_lines:
            counter = 0
            que.put(evaluate_card(full_card[0], full_card[1]))
            



if __name__ == "__main__":
    main()