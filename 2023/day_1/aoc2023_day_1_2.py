with open('day_1\input.txt', 'r') as input_file:
    input = input_file.read()

item_split = [n for n in input.split("\n")]
numbers_dict = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }

total_sum = 0
for item in item_split:
    if item == "":
        break
    print(f"SOURCE STRING: {item}")
    new_test_str = ""
    for character in item:
        new_test_str += character
        for key,value in numbers_dict.items():
            if key in new_test_str:
                new_test_str = new_test_str.replace(key,value+key[-1:])
    print(f"TEST STRING: {new_test_str}")
    digit = ""
    for character in new_test_str:
        if character.isdigit():
            digit += character
            break
    for character in new_test_str[::-1]:
        if character.isdigit():
            digit += character
            break
    print(f"NUMBERS: {digit}")
    total_sum += int(digit)
    print(f"SUM: {total_sum}")

print(f"TOTAL: {total_sum}")