import re

from utils.helpers import parse_input

product=0
pattern1=r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
pattern2="(do\(\)|don't\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\)"
lines = parse_input('../data/3_input.txt',True)
#lines = parse_input('../tests/3_test_input.txt',True)

print (lines)

part1_nums = re.findall(pattern1,lines)
#print (part1_nums)
for command in part1_nums:
    product += int(command[0])*int(command[1])
print('part 1 answer:',product)

part2_nums=re.findall(pattern2,lines)
print (part2_nums)
instr='do()'
sum=0
for i in part2_nums:
    #print (i[0])
    if i[0]=='' and instr=='do()':
        #print ('state is',instr, 'numbers are:',int(i[1]),int(i[2]),'multiplying')
        sum += int(i[1]) * int(i[2])
    if i[0]=='' and instr=="don't()":
        #print ('state is',instr, 'numbers are:',int(i[1]),int(i[2]),'skipping')
        pass
    if i[0]=='do()':
        instr='do()'
        #print ('setting state to do')
    if i[0]=="don't()":
        #print ('setting state to do not')
        instr = "don't()"
print ('part2 answer:',sum)

