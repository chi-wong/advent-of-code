with open('input.txt', 'r') as input_file:
    input = input_file.read()
item_split = [n for n in input.split("\n")]

digit_list = []
for item in item_split:
    digit = ""
    for character in item:
        if character.isdigit():
            digit += character
            break
    for character in item[::-1]:
        if character.isdigit():
            digit += character
            break
    digit_list.append(int(digit))
print(sum(digit_list))