def problem1(l , num ):
    result = []
    p1 = 0
    p2 = 1
    for i in range(len(l)): 
        while p1 < p2  and p2 < len(l): 
            if l[p1] + l[p2] == num: 
                result.append((l[p1], l[p2]))
                p2 += 1
        p1 += 1
        p2 = p1 + 1
    return result

print(problem1([1, 2, 3, 4, 5, 6] , 7))
        
         
        

# input: [1, 2, 3, 4, 5, 6] , 7
# output: 1,6 , 2,5 , 3, 4