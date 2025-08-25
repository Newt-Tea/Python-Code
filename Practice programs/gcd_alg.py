import pytest
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
#implement these as pytest unit tests

def test_gcd():
    assert gcd(78,55)==1
    assert gcd(25,85)==5
    assert gcd(899,713)==31
print("GCD of 78 and 55 is",gcd(78,55))
print("GCD of 25 and 85 is",gcd(25,85))
print("GCD of 899 and 713 is",gcd(899,713))
test_gcd()
