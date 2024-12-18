import re

product=0
pattern=r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
with open('3.txt', 'r') as file:
    lines = file.read()
    print (lines)

    commands=re.findall(pattern,lines)
    print (commands)
    for command in commands:
        product += int(command[0])*int(command[1])
print(product)