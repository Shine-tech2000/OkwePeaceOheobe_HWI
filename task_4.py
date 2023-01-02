# Read the number of elements to output from standard input
n = int(input())

# Initialize a variable to keep track of the current number
current_number = 1

#Initialize a counter to keep track of how many numbers have been output
counter = 0

# Keep outputting numbers until we have outputted the desired number of elements
while counter < n:
    # Output the current number the required number of times
    for i in range(current_number):
        print(current_number, end=" ")
        counter += 1

        #if we have outputed the desired number of elements break out of the loop
        if counter == n:
            break
    current_number += 1

#Add a new line after all the numbers have been printed
