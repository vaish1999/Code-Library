n = int(input('n = '))
ln = n * 2
paths = []
tokens = ['x', 'y']
paths.append('x')

for i in range(1, ln):
    new_path = []
    for idx, seq in enumerate(paths):
        for c in tokens:
            p = seq + c
            if p.count('x') >= p.count('y'):
                # print(p)
                new_path.append(p)
    # print(new_path)
    paths = new_path        

# print(paths)
j = 0
for p in (paths):
    if p.count('x') == p.count('y'):
        j+=1
        # print(p)

print('dyck paths:', j)
                



