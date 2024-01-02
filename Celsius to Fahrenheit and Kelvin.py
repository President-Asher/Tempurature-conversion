classoftemp = ''
asktemp = float
def Calculator():
    print("What is the tempurature?:")
    asktemp = float(input())
    print("Is that in Celcius, Fahrenheit, or Kelvin?")
    classoftemp = input("(Type C, F, or K): ")
    if classoftemp == 'C':
        print("Fahrenheit:")
        print(asktemp * 9/5 + 32)
        print("Kelvin:")
        print(asktemp + 273.15)
        Calculator()
    elif classoftemp == 'F':
        print("Celsius: ")
        print((asktemp - 32) * 5/9)
        print("Kelvin:")
        print((asktemp - 32) * 5/9 + 273.15)
        Calculator()
    elif classoftemp == 'K':
        print("Celsius:")
        print(asktemp - 273.15)
        print("Fahrenheit:")
        print((asktemp - 273.15) * 9/5 + 32)
        Calculator()
    else:
        print("That is not a valid Unit of Measurement...")
        Calculator()
Calculator()