if __name__ == "__main__":
    def gcd(a,b):
        n=max(a,b)
        m=min(a,b)
        r=-1
        while r!=0:
            r=n%m
            n=m
            m=r
        return n
    # a=int(input("Enter first number: "))
    # b=int(input("Enter second number: "))
    # print("GCD of",a,"and",b,"is",gcd())
    print("GCD of 78 and 55 is",gcd(78,55))
    print("GCD of 25 and 85 is",gcd(25,85))
    print("GCD of 899 and 713 is",gcd(899,713))
