from random import randint
arr=[]
for i in range (15):
    arr.append(randint(0,251))
print(arr)
b=arr.index(max(arr))
arr[b],arr[-1]=arr[-1],arr[b]
print(arr)
#тест версии



