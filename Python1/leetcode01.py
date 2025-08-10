nums=[1,3,4,6,9] #sum of  number and print the index that equals to target 
target=9
a=[]


for i in range (len(nums)):
    for j in range (i + 1,len(nums)):
        if nums[i] + nums[j] == target:
            a.append((i,j))
print(a)