a= int(input())
b= int(input())
c= int(input())
result = list(str(a*b*c)) # list사용
for i in range(10):
    print(result.count(str(i))) #count사용
