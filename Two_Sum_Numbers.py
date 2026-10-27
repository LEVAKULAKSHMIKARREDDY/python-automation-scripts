arr=[2,7,7,2,8,1,1,8]
target=9
seen=set()
pairs=[]
for i in arr:
    diff=target-i
    if diff in seen:
        pair=((min(diff,i),max(diff,i)))
        if pair not in pairs:
            pairs.append(pair)
    seen.add(i)
print(pairs)