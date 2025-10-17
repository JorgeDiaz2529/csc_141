from random import choice

lottery_list = [1,2,3,4,5,6,7,8,9,0,"a","b","c","f"]

lottery_number = f"{choice(lottery_list)}{choice(lottery_list)}\
{choice(lottery_list)}{choice(lottery_list)}"

print(f"Any ticket matching {lottery_number} is the winner!")

def make_ticket():
    ticket = f"{choice(lottery_list)}{choice(lottery_list)}\
{choice(lottery_list)}{choice(lottery_list)}"
    return ticket

count = 0
while True:
    current_ticket = make_ticket()

    if current_ticket == lottery_number:
        print(f"It took {count} tries to get the right number!")
        break
    else:
        count += 1
