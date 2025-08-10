vowles="aeiouAEIOU"
text=input("Enter the Sentence: ")
count=0

for i in text:
    if i in vowles:
        count +=1
print("total vowels:",count)