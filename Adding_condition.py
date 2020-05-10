import random

dice_rolls = 2
dice_sum = 0
for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    
if roll == 1:
    print(f'You rolled {roll}! Critical fail')
elif roll == 6:
    print(f'You rolled {roll}! Critical Success')
else:
    print(f'You rolled {roll}')
print(f'You have rolled a total {dice_sum}')
