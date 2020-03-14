def find_max_sliding_window(arr, window_size):
  result = []
  window = []
  index = 0
  while index < len(arr):
    while len(window) > 0 and arr[index] > arr[window[-1]]:
        window.pop()
    if window and window[0] <= index - window_size:
      window.pop(0)
    window.append(index)
    if index >= window_size - 1:
      result.append(arr[window[0]])
    index += 1

  return result


array = [-4, 2, -5, 3, 6]
array2 = []
# print(find_max_sliding_window([1, 2, 3, 4, 3, 2, 1, 2, 5],4))
print(find_max_sliding_window([1, 2, 3, 4, 3, 2, 1, 2, 5],10))
# print(find_max_sliding_window(array2, 3))