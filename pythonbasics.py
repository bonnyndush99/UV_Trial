number_of_bears=int(input("Enter the number of polar bears: "))
daily_ration=int(input("Enter the daily food ration per bear: "))
total_food = number_of_bears * daily_ration * 30
print(f"The food consumed is {total_food:,.1f} kg.")