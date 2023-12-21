with open('2023/day_4/input_test.txt', 'r') as input_file:
  input = input_file.read()
input_split = [item for item in input.split("\n")]

def winning_sum(x):
  sum = 0
  for i in range(0, x):
    sum = 2 ** i
  return sum

points = 0
total_scratchcards = []
for i,input in enumerate(input_split):
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

  for x in range(1,len(matched_numbers)+2):
    card_number = f"Card {x + i}"
    print(card_number)
    total_scratchcards.append(card_number)
  print(matched_numbers)
  points += winning_sum(len(matched_numbers))
  # print(points)
# print(points)
print(total_scratchcards)

# 1 2 3 4 5
#   3 
#   4