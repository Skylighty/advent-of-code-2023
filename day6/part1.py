from functools import reduce

def clear_input(strr):
    inputs = strr.split(':')[1]
    inputs = inputs.strip()
    inputs = inputs.split()
    inputs = [int(x) for x in inputs]
    return inputs


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    parameters = {t:d for t,d in zip(clear_input(lines[0]), clear_input(lines[1]))}
    times_to_win = []
    for t,d in parameters.items():
        temp = []
        for i in range(1, t+1):
            distance = i*(t-i)
            if distance > d:
                temp.append(i)
        spanstart, spanend = min(temp), max(temp)
        times_to_win.append(spanend-spanstart+1)
    sums = reduce(lambda x,y : x*y, times_to_win, 1)
    print(sums)
    
    
    
    
# CORRECT - 275724
    
    
if __name__ == "__main__":
    main()