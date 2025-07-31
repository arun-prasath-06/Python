num=[1,3,4,6,9] #sum of  number and print the index that equals to target 
target=5
result=[]

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == target:
            result.append((i,j))
print(result)