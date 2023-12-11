f = open("input.txt").readlines()

s = 0
cards = [1 for _ in f]
print(cards)
for index, line in enumerate(f):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    n = len(set(a) & set(b))
    
    for i in range(n):
        cards[index + i + 1] += cards[index]
        print(cards)

print( sum(cards))