from functools import reduce

def clear_input(strr):
    inputs = strr.split(':')[1]
    inputs = inputs.strip()
    inputs = inputs.split()
    inputs = ''.join(inputs)
    return int(inputs)


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    t = clear_input(lines[0])
    d = clear_input(lines[1])
    times_to_win = []
    for i in range(1, t+1):
        distance = i*(t-i)
        if distance > d:
            times_to_win.append(i)
    spanstart, spanend = min(times_to_win), max(times_to_win)
    result = len(range(spanstart,spanend+1))
    print(result)
    
    
if __name__ == '__main__':
    main()