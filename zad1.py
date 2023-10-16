#zadanie 1
# Napisz program, który pyta użytkownika (input) o imię oraz wiek a następnie wyświetla napisy:
# Cześć <imię>!
# Twoje imię ma <liczba liter imienia> liter i zaczyna się od <pierwsza litera imienia>
# Teraz masz <wiek> lat, a za rok będzie to <wiek za rok>. Rok urodzenia to <rok urodzenia>
import datetime

name = input("Enter your name: ")
age = input("Enter your age: ")
def current_year():
    now = datetime.datetime.now()
    return now.year

year = current_year()

if not name or not age or not age.isdigit() or name.isdigit() or name.isspace() or int(age) > int(year):
    print("Something gone wrong!")
else:
    def first_letter(name):
        if len(name) > 0:
            return name[0]
        else:
            return None
    birth_date = current_year() - int(age)

    next_year = int(age) + 1
    print("Hi,", name)
    print("Your name have", len(name), "letters, and begins with", first_letter(name))
    print("Now, you're", age, "and next year you will be", next_year)
    print("Your year of birth is", birth_date)