print('welcome')

# get the user input
date = input('What is the date? ')
mileage = input('What is the mileage? ')

# get the current mileage
with open('alternative_tracker.txt', 'r') as file:
    text = file.read()

# check the last updated mile total
last_item = text.split(',')[-1].strip()
if last_item.isdigit() and mileage.isdigit():
    total = int(last_item) + int(mileage)
else:
    total = 0

# construct the new line
new_line = '{}, {}, {}\n'.format(date, mileage, total)

# write ('append') the new line to the file
with open('alternative_tracker.txt', 'a') as file:
    file.write(new_line)

print('file saved')
