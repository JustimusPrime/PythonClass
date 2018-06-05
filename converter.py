print("Why hello, friendly user. I am a beta of Murderbot. In this early version, I can only convert miles to kilometers or vise versa.")
print("Which would you like to convert, miles or kilometers?")
choice = input().lower()


print(choice[0])

if choice[0] == "m":
    print("How many miles did you want to convert into kilometers?")
    miles = float(input())

    kilometers = miles * 1.60934

    print(f"{round(miles, 2)} miles would convert to {round(kilometers, 2)} km")
elif choice[0] == "k":
    print("How many kilometers did you want to convert into miles?")
    kilometers = float(input())

    miles = kilometers / 1.60934

    print(f"{round(kilometers, 2)} kilometers would convert to {round(miles, 2)} miles")

else:
    print("you didn't pick either bro, but I don't know how to loop yet so GOODBYE")









# print("How many miles did you want to convert into kilometers?")
# basic way, complicated below

# miles = float(input("How many miles did you want to convert into kilometers?"))
# complicated way, but puts them on the same line, first way looks cleaner in execution, second looks cleaner in code
# how you convert a data type
# kilometers = miles * 1.60934
# print(f"{round(miles, 2)} miles would convert to {round(kilometers, 2)} km")
# print(f"is string interpolation")
# wont work if not python3