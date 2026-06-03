# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. THe sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Project Euler

# Make an empty list and add multiples of 3 or 5 to the list using a for loop.
components = []

for i in range(0,1000):
  if i % 3 == 0:
    components.append(i);
  elif i % 5 == 0:
    components.append(i);
  else:
    pass;

components = list(set(components))
sum = sum(components)

print(sum)

# Lessons learned
# = is used to assign variable values, whereas == is used for numerical equality
# pass = do nothing
# list(set(mylist)) deletes duplicates in a list no matter the order
