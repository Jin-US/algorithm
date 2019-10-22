# https://www.acmicpc.net/problem/2588


a ,b = map(int, input().split())
for i in range(len(str(b))):
    # print( int( str(b)[ len( str(b) )-i-1 ] )*a )
    print(int(str(b)[len(str(b))-i-1])*a)





# print(
#     int(str(b)
#         [len(str(b))-i-1]
#         )*a
# )









# mul   : 각 단계 계산 과정    (result[])
#mul2   : 한줄 계산 결과 출력용  (result2[])

# def arr(A, B):
#     result =[0]
#     result2 =[]
#     temp =[0]
#     index = 1
#
#     for j in range(3, 0, -1):
#         mul2 = 0
#         for k in range(3, 0, -1):
#             mul = A[k-1] * B[j-1]
#             if(k<3):
#                 for k in range(k,3):
#                     mul = mul * 10
#             index += 1
#             mul2 = mul2 + mul
#             temp.insert(index, mul2)
#             result.insert(index, mul)
#         # temp = result[j]
#
#     for index in range(1,index):
#         if(index % 3 == 0):
#             temp2 = temp[index]
#             result2.insert(index, temp2)
#     temp2 = 0
#     for index in range(0,len(result2)):
#         # print(index)
#         if(index>0):
#             # print(index)
#             for i in range(0,3):
#                 result2[i] = result2[i] * 10
#         print(result2[index])
#         temp2 = result2[index] + temp2
#     print(temp2)
#
# A = input()
# A = A.split()
# A = list(map(int, A))
# B = input()
# B = B.split()
# B = list(map(int, B))
#
# arr(A, B)










# # mul   : 각 단계 계산 과정    (result[])
# #mul2   : 한줄 계산 결과 출력용  (result2[])
#
# def arr(A, B):
#     result =[0]
#     result2 =[]
#     temp =[0]
#     index = 1
#
#     for j in range(3, 0, -1):
#         mul2 = 0
#         for k in range(3, 0, -1):
#             mul = A[k-1] * B[j-1]
#             if(k<3):
#                 for k in range(k,3):
#                     mul = mul * 10
#             index += 1
#             mul2 = mul2 + mul
#             temp.insert(index, mul2)
#             result.insert(index, mul)
#         # temp = result[j]
#
#     for index in range(1,index):
#         if(index % 3 == 0):
#             temp2 = temp[index]
#             result2.insert(index, temp2)
#     temp2 = 0
#     for index in range(0,len(result2)):
#         # print(index)
#         if(index>0):
#             # print(index)
#             for i in range(0,3):
#                 result2[i] = result2[i] * 10
#         print(result2[index])
#         temp2 = result2[index] + temp2
#     print(temp2)
#
# A = input()
# A = A.split()
# A = list(map(int, A))
# B = input()
# B = B.split()
# B = list(map(int, B))
#
# arr(A, B)