hourly_rate_input = input("Enter the hourly rate: ")
print("Hourly rate:", hourly_rate_input, "usd")

hours_worked_input = input("Enter hours worked: ")
print("Hours worked:", hours_worked_input, "hours")

hourly_rate = float(hourly_rate_input)
hours_worked = float(hours_worked_input)

payment = hourly_rate * hours_worked
formatted_payment = "{:.2f}".format(payment)  # Formats the payment to have two decimal places
print("The corresponding payment is:", payment, "usd")
