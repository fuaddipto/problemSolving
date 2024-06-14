def sum_array(arr, size):
  """Calculates the sum of elements in an array

  Args:
      arr: The input array
      size: The size of the array

  Returns:
      The sum of the elements in the array
  """

  sum = 0
  for i in range(size):
    sum += arr[i]
  return sum

SIZE = 5
numbers = [0 for _ in range(SIZE)]

print("Enter", SIZE, "numbers:")
for i in range(SIZE):
  numbers[i] = int(input())

sum = sum_array(numbers, SIZE)
print("Sum of the elements:", sum)