def solve():
    s = input()
    regex = '[\w\s,:]+'
    l = re.findall(regex,s)

    for sentence in l:
        tmp = sentence.lower().split()
        st = tmp[0].title()
        for i in range(1, len(tmp)):
            if tmp[i] == ',' or tmp[i] == ':':
                st += tmp[i]
            else:
                st += ' ' + tmp[i]
        print(st)


import re

while True:
    try:
        solve()
    except:
        break