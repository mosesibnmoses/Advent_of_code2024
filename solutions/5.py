from collections import defaultdict

from utils.helpers import parse_input

#file=parse_input('../tests/5_test_input.txt')
file=parse_input('../data/5_input.txt')
rules = (file[:file.index('')])
sequences = (file[file.index('')+1:])

rules_list=defaultdict(list)
for rule in sorted(rules):
    num1,num2= rule.split('|')
    #print (num1,num2)
    rules_list[num1].append(num2)

#print (rules_list)
valid_seqs=[]
invalid_seqs=[]

def check_sequence(sequence_name):

    #print('\nseq', sequence_name)
    valid=True
    for i in (range(len(sequence_name))):
        page = sequence_name[i]
        #print(page)
        disallowed = rules_list[page]
        #print(page, 'cannot be preceded by', disallowed)
        preceding_pages = sequence_name[:i]
        #print('is preceded by', preceding_pages)
        violators = set(preceding_pages).intersection(set(disallowed))
        #print(len(violators), 'violators:', [violators])
        if len(violators) >= 1:
            #print('skipping sequence')
            return False

    if valid:
        #print('VALID')
        return True

for sequence in sequences:
    sequence = sequence.split(',')
    #check sequence
    if check_sequence(sequence):
        valid_seqs.append(sequence)
    else:
        invalid_seqs.append(sequence)
    #print (valid_seqs)

def reorder_sequence(sequence_name):
    changed = True
    corrected_sequence=sequence_name[:]
    while changed:
        for i in range(len(corrected_sequence)):
            #print ('looking at',corrected_sequence[i])
            changed=False
            page = corrected_sequence[i]
            #print(page)
            disallowed = rules_list[page]
            ##print(page, 'cannot be preceded by', disallowed)
            # Check for violators among preceding pages
            preceding_pages = corrected_sequence[:i]
            #print('is preceded by', preceding_pages)
            violators = [p for p in preceding_pages if p in disallowed]
            if violators:
                #print(len(violators), 'violators:', [violators])
                #print(f"Current sequence: {corrected_sequence}")
                max_violator_index = max(corrected_sequence.index(p) for p in violators)
                swapped_page = corrected_sequence[max_violator_index]

                corrected_sequence.insert(max_violator_index, corrected_sequence.pop(i))
                #print(f"Swapped '{page}' to resolve conflict with '{swapped_page}'.")
                #print(f"Current corrected sequence: {corrected_sequence}")
                changed = True
                break
    if not check_sequence(corrected_sequence):
        raise ValueError(f"Sequence cannot be reordered: {sequence_name}")
    return corrected_sequence

def find_middle_element(list_name):
    return int(list_name[len(list_name)//2])

print (valid_seqs)
print (invalid_seqs)

valid_middle_sum=0
for valid_seq in valid_seqs:
    valid_middle_sum+=find_middle_element(valid_seq)

print ('Part 1:',valid_middle_sum)
invalid_middle_sum=0
for invalid_seq in invalid_seqs:
    reordered_sequence=reorder_sequence(invalid_seq)
    invalid_middle_sum += find_middle_element(reordered_sequence)
print('Part 2:', invalid_middle_sum)

