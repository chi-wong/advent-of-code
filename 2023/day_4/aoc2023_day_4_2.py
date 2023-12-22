with open('2023/day_4/input_test.txt', 'r') as input_file:
  input = input_file.read()
input_split = [item for item in input.split("\n")]


points = 0
initial_scratchcards = []
scratchcard_copies = []

for i,input in enumerate(input_split):
  print(input[:8])
  initial_scratchcards.append(i+1)
  # new_input = input[10:]
  new_input = input[8:]
  new_input_split = new_input.split(" | ")
  winning_numbers = new_input_split[0].split(' ')
  while '' in winning_numbers:
    winning_numbers.remove('')
  my_numbers = new_input_split[1].split(' ')
  while '' in my_numbers:
    my_numbers.remove('')
  matched_numbers = list(set(winning_numbers).intersection(my_numbers))
  print(f"Card {i+1} wins copies of the following cards:")
  if len(matched_numbers):
    print(*range(i+2,len(matched_numbers)+(i+2)))
    scratchcard_copies.append([*range(i+2,len(matched_numbers)+(i+2))])
  # print(points)
# print(points)
print(initial_scratchcards)
total_scratchcards = initial_scratchcards
print(scratchcard_copies)


# The winning numbers instruct the next cards to multiply

# 1: 2 3 4 5
# 2: 3 4
# 2: 3 4
# 3: 4 5
# 3: 4 5
# 3: 4 5
# 3: 4 5
# 4: 5
# 4: 5
# 4: 5
# 4: 5
# 4: 5
# 4: 5
# 4: 5
# 4: 5
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 5: 
# 6: 