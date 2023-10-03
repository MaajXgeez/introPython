zoo_animals = ['wolf', 'giraffe', 'hippo', 'eagle', 'parrot']
sports_on_tv = ['hockey', 'football', 'baseball', 'soccer', 'racing']
random_numbers = [10, 100, 12123, 1394, 1]
print(zoo_animals[3])   # Index 3: 'eagle'
print(sports_on_tv[1])  # Index 1: 'football'
print(random_numbers[0]) # Index 0: 10
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a for loop to iterate through the list and print odd numbers
for num in number_list:
    if num % 2 != 0:
        print(num)
# Existing shopping cart list
shopping_cart = ['notebook', 'pens', 'tape', 'mousepad']

# Ask the user to enter a new item
new_item = input("Enter the item you want to add to the cart: ")

# Add the new item to the shopping cart
shopping_cart.append(new_item)

# Print the updated shopping cart
print("Updated Shopping Cart:")
for item in shopping_cart:
    print(item).



