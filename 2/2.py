from itertools import count

from pycparser.c_ast import Return


def eval_report(report: list) -> bool:
    """

    :rtype: bool
    """
    if sorted(report)==report or sorted(report,reverse=True)==report:
        max_difference = max([abs(b - a) for a, b in zip(report, report[1:])])
        min_difference = min([abs(b - a) for a, b in zip(report, report[1:])])
        if min_difference < 1 or max_difference > 3:
            return False
        else:
            return True
    else:
        return False

sum=0
with open('2.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(' ')
        line = [int(e) for e in line]
        if(eval_report(line)):
            sum+=1
print('part 1 answer:',sum)

#eval_report([1,3,6,7,9])
