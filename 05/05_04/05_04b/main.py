from collections import deque
import math

def print_binary(num):
  if num <= 0:
    return

  binary_queue = deque()
  i = 0
  while i <= num: 
     binary_queue.append(bin(i))
     i += 1
  
  while len(binary_queue) > 0:
    document = binary_queue.popleft()
    print(f'{document}')
  return

print_binary(5)
