def prime(m):
    for x in range(2,m):
        if m%x==0:
            return False
    return True
n = eval(input())
if n>int(n):
    n=int(n)+1
c=0
listz=list()
while c<5:
    if prime(n):
        c+=1
        listz.append(n)
    n+=1
print(str(listz).replace(' ','')[1:-1])