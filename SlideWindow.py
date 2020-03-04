def find_max_sliding_window(arr, window_size):
  result = []
  low = 0
  high = window_size
  while high <= len(arr):
      tempArray = []
      index = low
      while index < high:
        tempArray.append(arr[index])
        index += 1
      result.append(find_max_in_array(tempArray))
      low += 1
      high += 1

  return result

def find_max_in_array(array):
  if len(array) == 0:
    return None
  max = array[0]
  for number in array:
    if number > max:
      max = number
  return max


array = [-4, 2, -5, 3, 6]
print(find_max_sliding_window(array, 3))