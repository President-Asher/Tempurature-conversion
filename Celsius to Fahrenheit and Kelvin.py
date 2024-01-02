print("What is the tempurature?:")
asktemp = float(input())

classoftemp = input("Is that in Celcius or Fahrenheit?: ")
if classoftemp == 'Celsius' or 'celsius':
    print("Fahrenheit:")
    print(asktemp * 9/5 + 32)
    print("Kelvin:")
    print(asktemp + 273.15)
elif classoftemp == 'Fahrenheit' or 'fahrenheit':
    print("Celsius: ")
    print((asktemp - 32) * 5/9)
    print("Kelvin:")
    print((asktemp - 32) * 5/9 + 273.15)
else:
    print("That is not a valid Unit of Measurement...")