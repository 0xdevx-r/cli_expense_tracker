# CLI Expense Tracker
# Concept : Addition of items in category, cost, deleting items in category, update items in category

# Defining categories of the expense tracker

user_name = input("Enter First name: ")

print(f"Hi {user_name}!. Please select a task number from below mentioned: \t")
print("1. Household Expenses\n")
print("2. Medical Supplies\n")
print("3. Grocery\n")

user_input = " "

household_list = []
medical_supplies = []
grocery_list = []

while True:
    user_input = input("Select the number corresponding to the category: ")
    
    if not user_input.strip():
        print("⚠️ Error: No valid response received. Enter a valid response number.")
    
    elif not user_input.isdigit():
        print("⚠️ Please enter numbers only.")
    
    else:
        user_input = int(user_input)
        if user_input == 1:
            amount = float(input("Enter the amount: "))
            household_list.append(amount)
            print("Amount added successfully!")
            break

        elif user_input == 2:
            amount = float(input("Enter medical expense amount: "))
            medical_supplies.append(amount)
            print("Expense added successfully.")
            break
        
        elif user_input == 3:
            amount = float(input("Enter grocery expense amount: "))
            grocery_list.append(amount)
            print("Expense added successfully.")
            break
        else:
            print("⚠️ Invalid category number.")

print("\nHousehold Expenses:", household_list)
print("Medical Expenses:", medical_supplies)
print("Grocery Expenses:", grocery_list)