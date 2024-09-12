from collections import deque

def parentheses_match(my_string):
  parentheses_stack = deque()

  for c in my_string:
    if c == "(":
      parentheses_stack.append(c)
    elif c == ")":
      if not parentheses_stack:
          return False
      parentheses_stack.pop()
  return len(parentheses_stack) == 0


print(parentheses_match("()"))
print(parentheses_match("(()"))
print(parentheses_match(")("))
print(parentheses_match("(--)"))
print(parentheses_match("()-"))
print(parentheses_match("())"))