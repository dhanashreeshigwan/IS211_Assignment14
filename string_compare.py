def compareTo(s1, s2):
    if s1 < s2:
        return -1 
    elif s1 > s2:
        return 1
    else:
        return comapreChar(s1,s2)

def comapreChar(s1, s2):
    m = len(s1)
    if m == 0:
        return 0	
   
    if s1[0] == s2[0]:
        return comapreChar(s1[1:], s2[1:])


if __name__=="__main__":
    s1 = input("Enter First String:")
    s2 = input("Enter Second String:")
    str1 = s1.strip().lower()
    str2 = s2.strip().lower()
    res = compareTo(str1,str2)
    print("Result of comparion is : {0}".format(res))
