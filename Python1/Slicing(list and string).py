tup="Arun prasath"
print(tup[::-1])    #reverse printing
print(tup[1:5])     #printing the string index 2 to 4
print(tup[0:15:2])  #printing string from index by skipping 2
print(tup)          #print default value 
print(tup[4:])      #skipping first index and printing 0 to 4 index
print(tup[:4])      #skipping last index printing 0 to 4 index
print(tup[::4])     #printing the index by skippig 4(jumping)
a=[2,5,1,8,4]
print(a[2:4])

a[2:4]=[3,7]
print(a)