def find_max(a, b,c):
  max_number = a
  if a > b and a > c:
    max_number = a
  elif b > a and b > c:
    max_number = b
  else:
    max_number = c

  return max_number

#FREEZE CODE BEGIN
a = int(input("Enter a number:\n"))
b = int(input("Enter a number:\n"))
c = int(input("Enter a number:\n"))
#FREEZE CODE END

maximum = find_max(a,b,c)

print("Maximum value:", maximum)
