from collections import deque

def evaluate_card(card_list, index):
    wins = 0
    won_cards = []
    card = card_list[index-1]
    for winning_number in card[0]:
        if winning_number in card[1]:
            wins += 1
            won_cards.append(index+wins)
    if wins > 0:
        return won_cards
    else:
        return None


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    formatted_lines = []
    for index,card in enumerate(lines):
        winning, mine = card.split('|')
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
    
    # This one goes tricky 
    cards = [1 for i in range(len(formatted_lines))]
    for index, line in enumerate(formatted_lines):
        # Get number of won cards
        # set force conversion autosorts and allows for bitwise-operation
        wins = len(set(line[0]) & set(line[1]))
        for i in range(wins):
            cards[index + i +1] += cards[index]
    sums = 0
    for processings in cards:
        sums += processings
    print(sums)
# I had to use tips here...

if __name__ == "__main__":
    main()