arr=[2,7,1,8]
target=9
Empty_set=set()
for i in arr:
    diff=target-i
    if diff in Empty_set:
        print(diff,i)
    else:
        Empty_set.add(i)

