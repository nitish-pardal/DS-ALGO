def tower(N,n,a=1,b=2,c=3):
    if n==1:
        
        return(a,c)
    else:
        tower(N,n-1,a,c,b)
    if N==N:
        
        tower(N,n-1,b,a,c)
        print("move ",n,"th disk from ",a ,"to", c)
tower(4,5)