'''t=int(input())
n=[]
j=0
i=0
while i <(1000):
    n.append(j)
    print('N[{}] = {}'.format(i,j))
    if j<(t-1):
        j = j + 1
    else:
        j == t-1
        j = 0
    i = i + 1'''

t = int(input())

j = 0
for i in range(1000):
    print(f'N[{i}] = {j}')
    j += 1
    if j == t:
        j = 0