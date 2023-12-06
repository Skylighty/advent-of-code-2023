def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    sums = 0
    for line in lines:
        list_line = []
        for sign in line:
            if sign.isdigit():
                list_line.append(sign)
        #to_sum = [list_line[0], list_line[-1]]
        #joined = ''.join(to_sum)
        joined = f'{list_line[0]}{list_line[-1]}'
        in_int = int(joined)
        sums += in_int
    print(sums)

# CORRECT - 54601

if __name__ == "__main__":
    main()