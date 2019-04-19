
def fibonacci(num):
    if num < 0:
        print("Number should be greater than 0")
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

if __name__=="__main__":
    n = input("Enter Number:")
    res = fibonacci(n)
    print("{0}th Fibonacci number is - {1}".format(n, res))
