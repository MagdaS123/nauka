def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Wybierz operacje.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))


# tu wpisz swój kod :)

        if choice == '1':
            suma = add(num1, num2)
            print(suma)

        elif choice == '2':
            roznica = subtract(num1, num2)
            print(roznica)

        elif choice == '3':
            iloczyn = multiply(num1, num2)
            print(iloczyn)

        elif choice == '4':
            iloraz = divide(num1, num2)
            print(iloraz)
        break
    else:
        print("Błędna wartość, podaj poprawną")
