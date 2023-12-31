import random
def chooseColor():
    color = [['#706e40'], ['#45fc48'], ['#3f5efb'], ['#fc466b'], ['#224da7'], ['#23a226']]
    number = 0
    for col in color:
        number += 1
    for _ in range(number):
        random_choose = random.choice(color)
        return random_choose[0]
        
color = chooseColor()
print(color)