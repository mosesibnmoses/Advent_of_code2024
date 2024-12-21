from itertools import count

from utils.helpers import parse_input


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

part1_sum=0
part2_sum=0
lines = parse_input('../data/2_input.txt')

for line in lines:
    line = line.strip().split(' ')
    line = [int(e) for e in line]
    if(eval_report(line)):
        part1_sum+=1
        part2_sum+=1
    else:
        iterations = [line[:i] + line[i + 1:] for i in range(len(line))]
        iter_results=[]
        for iteration in iterations:
            iter_results.append(eval_report(iteration))
        if max(iter_results)==True:
            part2_sum+=1
print('part 1 answer:',part1_sum)
print('part 2 answer:',part2_sum)


#eval_report([1,3,6,7,9])
