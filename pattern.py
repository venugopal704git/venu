#n=int(input("enter the size"))
h=65
m=48
c=0
c1=0
def fun(n):
    for i in range(0,n,1):
        if i%2:
            for j in range(0,n,1):
                if j<=i:
                    l=chr(j+h)
                    print(l,end=' ')
        else:
            for k in range(0,n,1):
                if k<=i:
                    g=chr(k+m)
                    print(g,end=' ')

        print(' ')


#h=65
#m=48
n=int(input("enter the size"))
fun(n)
