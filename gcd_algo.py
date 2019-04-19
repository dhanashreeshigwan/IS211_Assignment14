def gcd(n1, n2):
    if n2 > n1:
        return gcd(n2, n1)

    if n1 % n2 == 0:
        return n2

    return gcd(n2, n1 % n2)

if __name__=="__main__":
    n1 = input("Enter First Number:")
    n2 = input("Enter Second Number:")
    res = gcd(n1,n2)
    print("GCD of {0} and {1} is - {2}".format(n1, n2, res))
