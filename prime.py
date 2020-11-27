x = input("Enter any number ")
for i in range(2,int(x)):
    if(int(x)%i==0):
        print("Not prime number")
        break
else:
    print("you enter the prime number") 
