def sum(n):
    if n==0:
        return 0
    smalloutput=sum(n-1)
    return n+smalloutput
n = int(input("enter the number "))
print(sum(n))