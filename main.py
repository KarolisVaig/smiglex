# This function adds two numbers
def sudetis(x, y):
    return x + y

# This function subtracts two numbers
def atimtis(x, y):
    return x - y

# This function multiplies two numbers
def daugyba(x, y):
    return x * y

# This function divides two numbers
def dalyba(x, y):
    return x / y


print("Pasirink operacija.")
print("1.Sudeti")
print("2.Minusuoti")
print("3.Dauginti")
print("4.Dalinti")

while True:
    # take input from the user
    choice = input("Pasirink (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Pasirink pirma skaiciu: "))
            num2 = float(input("Pasirink antra skaiciu: "))
        except ValueError:
            print("Negeras irasas. Ivesk skaiciu.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", sudetis(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", atimtis(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", daugyba(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", dalyba(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Darom kita skaiciavima? (taip/ne): ")
        if next_calculation == "ne":
          break
    else:
        print("Invalidas")