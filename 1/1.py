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
print('part one answer:',sum(difflist))

part2score=0
for num1 in leftlist:
    part2score+=rightlist.count(num1)*num1
print ('part 2 answer:', part2score)