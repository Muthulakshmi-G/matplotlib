def max_of_two(x,y):#find maximum number of two number
    

    if x>y:#if x is bigger
        return x #return x
    return y #otherwise return y



def max_of_three(x,y,z): #maximum number of 3 number
    return max_of_two(x,max_of_two(y,z))# it will gives max number of the above function
print(max_of_three(33,12,1)) #we give that three values to find max number
