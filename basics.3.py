user_age = input("Enter your age: ")
user_income = input("Enter your monthly income: ")
int_age = int(user_age)
int_income = int(user_income)

if int_age >= 16: 
    if int_income >= 1000:
        print("The user has to pay the tax")
    else:
        print("The user does not have to pay the tax")
else:
    print("The user does not have to pay the tax")