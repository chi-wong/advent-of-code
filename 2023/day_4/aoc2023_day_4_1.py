with open('2023/day_4/input.txt', 'r') as input_file:
  input = input_file.read()
input_split = [item for item in input.split("\n")]

def winning_sum(x):
  sum = 0
  for i in range(0, x):
    sum = 2 ** i
  return sum

i=1
points = 0
for input in input_split:
  new_input = input[10:]
  new_input_split = new_input.split(" | ")
  winning_numbers = new_input_split[0].split(' ')
  while '' in winning_numbers:
    winning_numbers.remove('')
  my_numbers = new_input_split[1].split(' ')
  while '' in my_numbers:
    my_numbers.remove('')
  matched_numbers = list(set(winning_numbers).intersection(my_numbers))
  points += winning_sum(len(matched_numbers))
  i+=1
print(points)