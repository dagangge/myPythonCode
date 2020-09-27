inputV=input()
for x in inputV[:]:
    if x==' ':
        print(" ",end='')        
    elif ord(x)>=ord('a') and ord(x)<ord('x'):
        x=chr(ord(x)+3)
        print(x,end='')        
    elif ord(x)>=ord('A') and ord(x)<ord('X'):
        x=chr(ord(x)+3)
        print(x,end='')
    elif x in ['x','y','z','X','Y','Z']:
        x=chr(ord(x)-23)
        print(x,end='')
    else:
        print(x,end='')
        


s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z': 
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
    elif 'A'<=c<='Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c
print(t)