from datetime import datetime


def check_birthday(name, birthdate):
    #Convert the birthdate string to a datetime object
    birthdate= datetime.strptime(birthdate,"%d-%m-%Y").date()

    # Get today's date
    today= datetime.now().date()

    if birthdate.month == today.month and birthdate.day == today.day:
        print(f"Happy birthday, {name}")
    else:
        print(f"Hi,{name} Today is not your birthday. Have a great day!")
def main():
    name= input("Enter the name of the person:")
    birthdate= input("Enter their birthdate (DD-MM-YYYY): ")

    check_birthday(name, birthdate)

if __name__=="__main__":
    main()
