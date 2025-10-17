from random import choice

lottery_list = [1,2,3,4,5,6,7,8,9,0,"a","b","c","f"]

lottery_number = f"{choice(lottery_list)}{choice(lottery_list)}\
{choice(lottery_list)}{choice(lottery_list)}"

print(f"Any ticket matching {lottery_number} is the winner!")
