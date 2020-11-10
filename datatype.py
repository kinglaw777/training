# 資料: 程式的基本單位
# 數字
3456
3.5
# 字串 ，在雙引號之內可以輸入任意文字，不帶雙引號直接打中文是不行的
"測試中文"
"Hello"
# 布林值
True
False
# List，是有順序可動的列表
[3,4,5]
["Hello","world"]
# Tuple，有順序且不可動的列表
(3,4,5)
("Hello","World")
# Set，集合 (沒有順序)
{3,4,5}
{"Hello","World"}
# Dictionary ，字典，冒號前的key對應到冒號後的值
{"apple":"蘋果","data":"資料"}
# 變數: 用來儲存資料的自訂名稱
# 變數名稱=資料
x=3
y=[1,2,3]
# print(資料) 印出資料
print(x)
print(y)
print(True)

# 同一個變數可以再放進不同的資料來變更，例如前面x=3，這裡我重新定義x=True，x的資料就會被取代
x=True
print(x)
x={3,4,5} # set 集合
print(x)
