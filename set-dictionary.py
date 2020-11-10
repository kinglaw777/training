# 集合的運算
s1={3,4,5}
print(3 in s1) # 3如果在 s1之中則為ture
print(10 not in s1) # 10如果不在 s1之中則為true
s2={4,5,6,7}
s3=s1&s2  # s1交集s2，交集:取兩個集合中，相同的資料 
print(s3)
s4=s1|s2  # 聯集: 取兩個集合中的所有資料，但不重複
print(s4)
s5=s1-s2  # 差集: 從s1中，減去和s2重疊的部分
print(s5)
s6=s1^s2  # 反交集: 取兩個集合中，不重疊的部分
print(s6)
s=set("Hello") # set(字串)，將字串拆解成集合
print(s)
print( "A" in s)

# 字典的運算: key-value 配對
dic={"apple":"蘋果", "bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic) # 判斷 key 是否存在
print("test" not in dic)
del dic["apple"] # 刪除字典中的鍵值對 (key-value)
print(dic)
dic2={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
print(dic2)