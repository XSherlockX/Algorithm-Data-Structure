#A bear has hidden n pieces of meat with sizes 1 to n in a cave. This bear every day
#A random person sleeps on a piece of meat and if it is an odd size, he eats the whole meat and if
#If the size of the meat is even, he eats half of the meat and saves the other half. The day these meats run out
#The bear dies. How many days does this bear live?

#Solutions:

import random


def bear_meat_survival(n):
    
    meats = list(range(1, n + 1))

    
    days_survived = 0

    while meats:
        
        days_survived += 1

        
        meat = random.choice(meats)

        if meat % 2 == 1:
            
            meats.remove(meat)
        else:
            meats[meats.index(meat)] = meat // 2

    return days_survived

meat = int(input())
print(bear_meat_survival(meat))
