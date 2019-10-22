# numbers = list(input().split())
# numbers.sort()
# print(numbers[1])

# 12 5 7    ->  12 5 7  => 앞 숫자기준??
# numbers = list(input().split())
# numbers.sort()
# for i in range(0,len(numbers)):
#
#     # numbers[i] = int(numbers[i])
#     print(numbers,type(numbers[i]))
#
# print(numbers[1])


# 11 22 12입력시 오류 22출력함. ,21 7 31 입력시 7출력
numbers = list(input().split())
numbers.sort(key=int)
print(int(numbers[1]))


# sorted(numbers)   => str순으로 정렬 EX) 12 < 5
# sorted(numbers,key=int)   => 정렬 타입 모르겠음   , 값 반환 안됨