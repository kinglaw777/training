# 判斷式
x=input("請輸入數字: ") #取得字串形式的使用者輸入
x=int(x) #將字串轉換成數字型態，才能進行比較
if x>200:    
    print("大於 200")
elif x>100:
    print("大於 100")
else:
    print("小於 100")

# 四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
print(n1+n2)
op=input("請輸入運算: +, -, *, /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援運算")