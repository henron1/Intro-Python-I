# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
def evens(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if evens(num):
    print("Even!")
else:
    print("Odd!")
# YOUR CODE HERE

