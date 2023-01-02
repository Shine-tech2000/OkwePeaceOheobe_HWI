# Initialize a variable to store the sum of numbers
Sum = 0

# Read numbers from standard input, one per line
while True:
    n = int(input())
    # if the number is zero, break out of he loop
    if n == 0:
        break
    Sum += n
print(Sum)
