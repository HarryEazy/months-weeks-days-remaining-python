
age = input("What is your current age? ")

average_age = 90
age_int = int(age)
years_left = 90 - age_int

days_remaining = 365 * years_left
weeks_remaining = 52 * years_left
months_remaining = 12 * years_left

message = f" You have {days_remaining} days left\n You have {weeks_remaining} weeks left\n You have {months_remaining} months left\n Take care!"


print(message)
