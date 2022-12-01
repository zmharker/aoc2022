with open('input.txt','r') as input:
    food_items = [int(i) if i != '\n' else 0 for i in input.readlines()]
    elf_counts = []
    current_sum = 0
    for i in range(0,len(food_items)-1):
        if food_items[i] == 0:
            elf_counts.append(current_sum)
            current_sum = 0
        else:
            current_sum = current_sum + food_items[i]
    # print(elf_counts)
    print(f'max sum: {max(elf_counts)}')

    sorted_elf_counts = sorted(elf_counts)
    # print(sorted_elf_counts)
    top_elf_len = 3
    top_elf_counts = sorted_elf_counts[(-1)*top_elf_len:]
    # print(top_elf_counts)
    sum = sum(top_elf_counts)
    print(f'top {top_elf_len} elves are carrying a total of {sum} calories')

