num = int(input())
temp = num
for i in range(0, num):
    num = num-1
    temp = temp + num
print(temp)