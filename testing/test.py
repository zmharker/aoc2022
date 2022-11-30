
with open('test_input.txt','r') as input:
    depths = input.readlines()
    depths = [int(d) for d in depths]
    print(f'parsed {len(depths)} inputs')
    increases = 0
    for i, depth in enumerate(depths):
        if i > 0:
            if depth > depths[i-1]:
                increases = increases + 1
    print(increases)

    sliding_sums = [depths[i] + depths[i+1] + depths[i+2] if i+2 < len(depths) else 0 for i, depth in enumerate(depths)]
    sum_increases = 0
    for j, sum, in enumerate(sliding_sums):
        if j > 0:
            if sum > sliding_sums[j-1]:
                sum_increases = sum_increases + 1
    print(f'sum increases: {sum_increases}')


