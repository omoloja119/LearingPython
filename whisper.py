is_hot = False
is_cold = False
if is_hot:
    print("its's hot")
    print('drink plenty of water')
elif is_cold:
    print("its's a cold day")
    print("wear thick cloths")
else:
    print("it's a lovely day")
print('enjoy your day')

price = 1000000
has_good_credit = False

if has_good_credit:
     down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'down payment: ${down_payment}')
has_good_credit = False
has_good_high_income = True
criminal_record = False
if has_good_credit or has_good_high_income and not criminal_record:
    print("eligible for loan")

temperature = 60
if temperature <= 40:
    print("it's a hot day")
else:
    print("it's not a hot day")

name = "whisper"
if len(name) < 9:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be max of 50 characters")
else:
    print("name looks good")

user_weight = int(input('weight: '))
unit = input('(k)g or l(bs): ')
if unit.upper() == 'L':
    converted = user_weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = user_weight / 0.45
    print(f'you are {converted} pounds')
x = (2 + 3) * 10 - 3
print(x)

e = 1
while e <= 5:
    print('$' * e)
    e = e + 1
print("done")

secret_number = 8
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
       print('Hey you won')
       break
else:
    print('Sorry you lose')

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit the game
        """)
    elif command == "quit":
        break
    else:
        print("sorry i don't understand")


for name in ['Yusuff' , 'Rahma' , 'Zainab' , 'Qasim' , 'Aisha' , 'Ahmad' , 'adburrahman' ]:
    print(name)

for item in range(0, 15, 3):
    print(item)

prices = [4, 5, 7, 10]
total = 0
for item in prices:
    total += item
print(f'Total: {total}')


numbers = [6, 3, 5, 2, 2]
for items in numbers:
    output =''
    for count in range(numbers):
        output += 'o'
    print(output)