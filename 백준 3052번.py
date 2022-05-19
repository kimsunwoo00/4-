arr=[]
for i in range(10):
    n = int(input())
    arr.append(n%42)
arr=set(arr) #set함수 사용 중복제거할수있음
print(len(arr))
