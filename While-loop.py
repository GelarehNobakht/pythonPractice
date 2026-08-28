#Even sum
i=0
limit= 100
summationEven=0
while i < limit:
    i+=2
    summationEven+=i

print(summationEven)

i=1
summationOdd=0
while i<limit:
    summationOdd+=i
    i+=2
print(summationOdd)


i=1
multiplication=1
limit = 5
while i<=limit:
    multiplication*=i
    i+=1
print(multiplication)



pattern = "+"
i=1
limit = 5
count = 1
while i>0:
    print(i * pattern)
    if i== limit:
        count =-1
    i+=count



#FACTORIAL
i=1
limit = 5 
result=1
while i <= limit:
    result= result *i
    i+=1
print(result)


#fibonacci 
i=0
j=1
next=0
limit = 10
result=0
count=0
while count<=limit:
    result +=i
    next=i+j
    i=j
    j=next
    count+=1
print(result)
