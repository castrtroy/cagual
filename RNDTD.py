import random

count = 0
circle = 1
while circle <= 100 :
    i = 1
    _ = 1
    m = []

    while i <= 7 :
        a = random.randint(1, 60)
        if a in m :
            i = i - 1
        else :
            m.append(a)
        #print(a)
        i = i + 1
    m4 = []
    while _ <= 4 :
        a = random.randint(1, 60)
        if a in m4 :
            i = i - 1
        else:
            m4.append(a)
        _ = _ + 1
    circle = circle + 1
    # print (m)
    # print (m4)
    result=list(set(m) & set(m4))
    # print (result)
    if len(result) > 0 :
        count = count + 1
        print (count)