import collections
import re
from collections import defaultdict

from utils.helpers import parse_input

file=parse_input('../tests/5_test_input.txt')
rules = (file[:file.index('')])
sequences = (file[file.index('')+1:])

rules_list=defaultdict(list)
for rule in sorted(rules):
    num1,num2= rule.split('|')
    print (num1,num2)
    rules_list[num1].append(num2)

print (rules_list)
valid_seqs=[]
for sequence in sequences:
    valid=True
    sequence=sequence.split(',')
    print('\nseq',sequence)
    for i in (range(len(sequence))):
        page=sequence[i]
        print (page)
        disallowed=rules_list[page]
        print(page,'cannot be preceded by',disallowed)
        preceding_pages=sequence[:i]
        print ('is preceded by', preceding_pages)
        violators=set(preceding_pages).intersection(set(disallowed))
        print (len(violators),'violators:',[violators])
        if len(violators)>=1:
            print ('skipping sequence')
            valid=False
            break
    if valid:
        print ('VALID')
        valid_seqs.append(sequence)
    print (valid_seqs)

def find_middle_element(list):
    return int(list[len(list)//2])

print (valid_seqs)

middle_sum=0
for valid_seq in valid_seqs:
    middle_sum+=find_middle_element(valid_seq)

print (middle_sum)