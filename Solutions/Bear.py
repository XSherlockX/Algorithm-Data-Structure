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