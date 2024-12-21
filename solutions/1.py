from utils.helpers import parse_input



def process_lines(lines):
    leftlist=[]
    rightlist=[]

    for line in lines:
        num1=int((line.strip().split(' ')[0]))
        num2=int((line.strip().split(' ')[-1]))
        leftlist.append(num1)
        rightlist.append(num2)
    return sorted(leftlist),sorted(rightlist)

lines = parse_input('../data/1_input.txt')
leftlist,rightlist=process_lines(lines)
difflist = [abs(a-b) for a,b in zip (leftlist,rightlist)]
print('part one answer:',sum(difflist))

part2score=0
for num1 in leftlist:
    part2score+=rightlist.count(num1)*num1
print ('part 2 answer:', part2score)