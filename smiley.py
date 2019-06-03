smiley = '\U0001f600'

num_lines = input("Pyramid size? ") 
num_lines = int(num_lines)

for num in range(0, num_lines):
    num_spaces = num_lines - num - 1
    num_smileys = 1 + (num * 2)
    print(num_spaces * ' ' + num_smileys * smiley)