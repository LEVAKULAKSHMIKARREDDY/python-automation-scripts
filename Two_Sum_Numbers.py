arr=[2,7,7,2]
target=9
Empty_set=set()
for i in arr:
    diff=target-i
    if i not in Empty_set:
        print(diff,i)
        Empty_set.add(diff)
        Empty_set.add(i)


    
    
    

