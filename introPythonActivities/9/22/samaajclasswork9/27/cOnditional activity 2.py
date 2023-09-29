# 1. Write a function that uses a conditional statement. 
# Your function should return a message that will determine if
# class is over or not depending on the argument passed into your function.
# IF the time of class is greater than 11.30 (for AP section) or
# 1.00(for intro), your funcion should return a message saying 
# "class is over. Time to go". 
# ELSE if it is not, then your function should return a message saying
# "class is still in session."
# your function should also allow the user to put in the time. The time should be 
# formatted as a float.
def check_class_status(class_time, section_type):
    if (section_type == "AP" and class_time > 11.30) or (section_type == "intro" and class_time > 13.00):
        return "Class is over. Time to go."
    else:
        return "Class is still in session."

# Example usage:
class_time = float(input("Enter the current time (e.g., 11.45 for 11:45 AM): "))
section_type = input("Enter the section type (AP or intro): ").lower()

result = check_class_status(class_time, section_type)
print(result)





# 2. Write a function that uses a conditional statement. 
# your function should determine what type a pet a user has depeding on the data provided by the user
# passed into the functions argument. 
# IF the user types in "woof", the function should return a message saying that it is a dog.
# IF the user types in "meow", the function should return a message saying that it is a cat.
# ELSE, if it is none of the animal sounds the function should return a message saying it doesn't 
# know what the animal is. 
def determine_pet_type(sound):
    if sound == "woof":
        return "It is a dog."
    else sound == "meow":
        return "It is a cat."
    else:
        return "It doesn't know what the animal is."

# Example usage:
user_input = input("Enter the sound your pet makes: ")
result = determine_pet_type(user_input)
print(result)


# 3. Write a function that will take in a user name and height as parameters. 
# Your function should evaluate and determine if the user is tall in enough to get on a roller coster.
# IF the user is over 5.5, the function should return a custom message saying the user's name
# and a message "welcome please buckle up".
# ELSE if they they are not, return a message apologizing to the user saying they are not tall enough.
def check_roller_coaster_eligibility(username, height):
    if height > 5.5:
        return f"Welcome {username}, please buckle up."
    else:
        return f"Sorry {username}, you are not tall enough to ride the roller coaster."

# Example usage:
user_name = "John"
user_height = 6.0
result = check_roller_coaster_eligibility(user_name, user_height)
print(result)  # Output: "Welcome John, please buckle up." 
