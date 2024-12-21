import re

from utils.helpers import parse_input

product=0
pattern=r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
lines = parse_input('../data/3_input.txt',True)
print (lines)
commands=re.findall(pattern,lines)
print (commands)
for command in commands:
    product += int(command[0])*int(command[1])
print(product)