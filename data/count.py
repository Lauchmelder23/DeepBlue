count=0
with open('naughty_step.txt', 'r') as file:
    for line in file:
        count += len(line)
print(count)
