def find_max_sliding_window(arr, window_size):
  result = []
  window = []
  index = 0
  while index < len(arr):
    currentNumber = arr[index]
    while len(window) > 0 and currentNumber > arr[window[len(window) - 1]]:
        window.pop()
    window.append(index)
    if window[0] <= index - window_size:
      window.pop(0)
    if index >= window_size - 1:
      result.append(arr[window[0]])
    index += 1

  return result



array = [-4, 2, -5, 3, 6]
array2 = []
print(find_max_sliding_window([1, 2, 3, 4, 3, 2, 1, 2, 5],4))
# print(find_max_sliding_window(array2, 3))