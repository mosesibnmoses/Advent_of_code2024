leftlist=[]
rightlist=[]
with open('1.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    print (line)
    num1=int((line.strip().split(' ')[0]))
    num2=int((line.strip().split(' ')[-1]))
    leftlist.append(num1)
    rightlist.append(num2)
leftlist.sort()
rightlist.sort()

difflist = [abs(a-b) for a,b in zip (leftlist,rightlist)]
print(sum(difflist))