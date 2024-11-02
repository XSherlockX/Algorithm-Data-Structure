def Binary_search(input, a):


    first = 0 
    last = len(input) - 1
    
    #-------------Binary Search------------


    while first <= last:
        mid = (first + last) // 2 #taghsim mikonim bar 2
        
        
        if input[mid] == a:
            return input[mid] 
        elif input[mid] < a: # aghar mid az adad ma kochiktar bod
            first = mid + 1
        else:
            last = mid - 1 # aghar mid az adad ma bizirgtar bod
    
    return "Not Found"



#Inputs:

array = list(map(int, input().split()))
target = int(input())


result = Binary_search(array, target)

#Output:

print(result)
