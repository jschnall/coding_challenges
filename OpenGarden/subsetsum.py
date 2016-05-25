'''
Created on Mar 6, 2015

@author: jschnall
'''
import itertools

def power_set(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def subset_sum(goal, items):
    memo = {}
    pow = power_set(items)
    for s in pow:
        subset = s[:len(s)-1]
        if subset in memo:
            set_sum = memo[subset] + s[len(s)-1]
        else:
            set_sum = sum(s)
        if set_sum == goal:
            return s
        memo[s] = set_sum
        
def exercise():
    target = 100000000
    pops = (18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411)
    new_target = sum(pops) - target    
    result = subset_sum(new_target, pops)
    answer = [item for item in pops if item not in result]
    print 'set: ' + str(answer)
    print 'sum: ' + str(sum(answer))