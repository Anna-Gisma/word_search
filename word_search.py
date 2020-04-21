def WordSearch(lenn, s, subs):
    l_str = []
    a = []
    c = 0 
    ind = 0 
    x = 0
    k = []
    for j in range(len(s)//lenn +1):
        a = []
        x = lenn + ind
        c = 0
        if x > len(s):
            x = len(s) 
        for i in range(ind, x):
            a.append(s[i])
            if s[i] == ' ':
                ind = i+1
                c += 1
            if c == 0:
                ind = i + 2
        a_str = ''.join(a)
        l_str.append(a_str)
    
    for i in range(len(l_str)):
        if (((subs + ' ' or ' ' + subs + ' ' or ' ' + subs ) in l_str[i]) or
            (len(subs) == len(l_str[i]) and subs in l_str[i])):
            k.append(1)
        else:
            k.append(0)

            
    return k

print(WordSearch(12, '1) строка разбивается на набор строк через выравнивание заданной ширине.', 'заданной'))        
    
            
    

       
