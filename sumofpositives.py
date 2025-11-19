# First step: define all your values and make your initial list into a global to be used in functions.
global my_list
my_list = []

global pos_sum
pos_sum = 0

a = 0
b = 0
c = 0
d = 0
e = 0

# Second step: create def
def sum_of_positives(my_list):

    # Access global list
    global pos_sum

    # Modify variables and display
    a = float(input("Please enter first number: "))
    b = float(input("Please enter second number: "))
    c = float(input("Please enter third number: "))
    d = float(input("Please enter fourth number: "))
    e = float(input("Please enter fifth number: "))
    my_list = [a,b,c,d,e]
    print("List of numbers: ",my_list)

    # Separate positives, display  and add them together.
    pos_list = []
    if a > 0:
        pos_list.append(a)
    if b > 0:
        pos_list.append(b)
    if c > 0:
        pos_list.append(c)
    if d > 0:
        pos_list.append(d)
    if e > 0:
        pos_list.append(e)
    print("List of positive values: ",pos_list)
    pos_sum += sum(pos_list)
    
    # Print sum
    print("The result is ", pos_sum)

# Third step: run function
sum_of_positives(my_list)
