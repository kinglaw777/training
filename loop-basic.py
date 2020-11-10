# while 迴圈
n=1
while n<=3:
    print(n)
    n+=1
# 1+2+3+....+10
n=1
sum=0
while n<=10:
    sum=sum+n
    n+=1 
print(sum)

# for 迴圈
for x in [3,5,1]:
    print("x為",x)

for y in "Hello":
    print("y為",y)

for z in range(5):  #range(5)等於[0,1,2,3,4]
    print("z為",z)

for q in range(5,10):  #range(5,10)等於[5,6,7,8,9]
    print("q為",q)

#改用for 迴圈作出 1加到10
sum=0
for x in range(1,11):
    sum=sum+x
print(sum)