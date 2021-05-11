def start():
    import time
    i=0
    while i<3:
        print("input N")
        N=int(input('>'))
        fun1(N)
        fun2(N)
        fun3(N)
        time.sleep(2)
        i=i+1

def fun1(N):
    sum1=0
    for n in range(1,2*N+1):
        sum1=sum1+((-1)**n)*(n/(n+1))
    print("Sum1 is:",sum1)

def fun2(N):
    sum2=0
    for n in range(1,N+1):
        sum2=sum2-((2*n)-1)/(2*n)
    #print(sum2)
    for k in range(1,N+1):
        sum2=sum2+((2*k)/(2*k+1))
    print("Sum2 is:",sum2)
    
def fun3(N):
    sum3=0
    for n in range(1,N+1):
        sum3=sum3+(1/((2*n)*(2*n+1)))
    print("Sum3 is:",sum3)

#Main Program
start()