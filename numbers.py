n1=int(input("enter first number :"))
n2=int(input("enter second number :"))
n3=int(input("enter third number :"))
def biggest(n1,n2,n3)
    if (n1 > n2) and (n1 > n3):
    largest = n1
    elif (n2 > n2) and (n2 > n3):
    largest = n2
    else:
    largest = n3
    return largest

print(biggest(10,20,30))
