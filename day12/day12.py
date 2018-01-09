from collections import *

#Special thanks to Arnav Sastry
# https://www.youtube.com/watch?time_continue=179&v=_nI5uCcBTcs

#For teaching me with his video about lambda, map and the solution to part1. :) Cheers!

handle = open("input.txt")

def part1():
    q = [0]
    vis = set()
    while q:
        a = q.pop()
        for b in graph[a]:
            if b not in vis:
                vis.add(b)
                q.append(b)
    print("Length of Group \"0\" is : " , len(vis))

def part2():
    ans = 0
    vis = set()
    for g in graph:
        if g in vis:
            continue
        ans +=1
        q = [g]
        while q:
            a = q.pop()
            for b in graph[a]:
                if b not in vis:
                    vis.add(b)
                    q.append(b)
    print("Nubmer of groups : " , ans)

graph = defaultdict(list)
for line in handle:
    words = line.rstrip().split()
    a = int(words[0])
    bs = map (lambda x: int(x.strip(",")) , words[2:])
    for b in bs:
        graph[a].append(b)

part1()
part2()
handle.close()
