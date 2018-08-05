# Q no 1: Write a python program to find number of occurrences of given number in a list with out using built-in methods
# **1 generate a list of some random num which is repeated again and again
# **2 take user input any number
# **3 find the number of occurrences of that num in your list
# **4 print some message to user with that result

nums = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]
num_to_find = int(input("Enter a number to find: "))
no_of_occurance = 0
for num in nums:
    if num == num_to_find:
        no_of_occurance += 1

print(f"The number {num_to_find} occured {no_of_occurance} times")

# Q no 2: ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# Write a python program to print website suffixes (com , org , net ,in) from this list

#%%
hosts = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
for host in hosts:
    print(host.split('.')[-1])

#   Q no 3 : Write a program which can compute the factorial of a given numbers.
# **1 first take user input any number
# **2 calculate factorial of that input and then print the result to us

def calculate_factorial(number):
    factorial = 1
    for num in range(1,number+1):
        factorial *= num
    return factorial

num = int(input("Enter a number to calculate it's factorial: "))
factorial = calculate_factorial(num)
print(f"The factorial of {num} is {factorial}.")

# Q 4 (a) : If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
list_of_guests = ["Alpha", "Beta", "Gamma"]
for guest in list_of_guests:
    print(f"Hey {guest}, You are invited for a dinner! Please do come.")

# Q 4 (b) : You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Q 4 (a). Add a print statement at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

print("Alpha can't make it.")
list_of_guests = ['Delta' if x=='Alpha' else x for x in list_of_guests]
for guest in list_of_guests:
    print(f"Hey {guest}, You are invited for a dinner! Please do come.")

# Q 4 (c) : You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Q 4 (a) and (b) Add a print statement to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print("Yay! We've found a bigger table.")
list_of_guests.insert(0 , "Epsilon")
list_of_guests.insert(len(list_of_guests)//2 , "Zeta")
list_of_guests.append("Eta")
for guest in list_of_guests:
    print(f"Hey {guest}, You are invited for a dinner! Please do come.")

# Q 5 : Here you have some data in variable below, your task is to make a list of specific word Surah then print the list and length of list
data = "Sura I Who believe in the Unseen, Sura Are steadfast in prayer, And spend Sura out of what We Have provided for them;"
data_list = data.split()
sura_list = []
for item in data_list:
    if item == 'Sura':
        sura_list.append(item)

print(sura_list)
print(f"Length of Sura list: {len(sura_list)}" )