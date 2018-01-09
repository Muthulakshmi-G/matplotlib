

#---------------
#simulating rolling a n sided die multiple times
#----------
import random



def rollDie(numberOfSides):
    """rolls an n-sided die
       pre condition:number of sides must be known as passed      	to the function    
     post-condtion:return a random value from 1 to n
    """

    rollValue=random.randint(1,numberOfSides)
    return rollValue
def main():
    random.seed()
    for x in range(0,10):
        print(rollDie(16))

if __name__=='__main__':
    main()
