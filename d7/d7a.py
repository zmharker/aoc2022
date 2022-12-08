def summarize_file(file_string):
    a = file_string.split()
    return {'size': int(a[0]), 'name':a[1]}

def parent_path(cd):
    a = cd.split('/')[0:-1]
    path = '/'.join(a)
    if path == '':
        path = '/'
    return path

def sum_files(files):
    file_sizes = [x['size'] for x in files]
    return sum(file_sizes)

MAX_SIZE = 100000

with open('input.txt','r') as input:
    lines = [x.strip() for x in input.readlines()]
    # print(lines)

    # build flattened tree
    tree = {'/': {'files': []}}
    cd = '/'
    list_mode = False

    for line in lines:
        if line[0] == '$':
            list_mode = False
            if line[2:5] == 'cd ':
                if line[5:] == '..': 
                    # go up a level
                    cd = parent_path(cd)

                elif line[5:] == '/':
                    cd = '/'

                else:
                    if cd == '/':
                        cd = cd + line[5:]
                    else:
                        cd = cd + '/' + line[5:]
                        if cd not in tree:
                            tree[cd] = {'files': []}
                    
                print(f'new cd: {cd}')
            
            elif line [2:] == 'ls':
                list_mode = True

        elif list_mode == True:
            if line[0:3] != 'dir':
                try:  
                    tree[cd]['files'].append(summarize_file(line))
                except KeyError:
                    tree[cd] = {'files': []}
                    tree[cd]['files'].append(summarize_file(line))

    print(tree, '\n')


    totals = {}
    for directory in tree:
        for (k,v) in tree.items():
            if directory in k:
                try:
                    totals[directory] += sum_files(v['files'])
                except KeyError:
                    totals[directory] = 0
                    totals[directory] += sum_files(v['files'])
            try:
                num_files = len(v['files'])
            except:
                num_files = 0
            print(f'{k} {num_files} files')


    grand_total = 0
    for (k,v) in totals.items():
        print(f'{k} {v}')
        if v <= MAX_SIZE:
            grand_total += v
            print(f'total increase: {grand_total}')
    print(f'\ngrand total: {grand_total}')

    



