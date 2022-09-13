import random
m=array('i',[1,2,3,4])
masiv=[]
x=0
for elem in range (8):
    x=random.randint(0,100)
    masiv.append(x)
for elem in range (8):
    print("1=",masiv[elem])
masiv1=[]
i=7
elem=0
for elem in range (8):
    x=masiv[i]
    masiv1.append(x)
    i=i-1
for elem in range (8):
    print("2=",masiv1[elem])