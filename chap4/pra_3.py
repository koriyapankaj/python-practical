# welcome to the chapter 4 practical 3

temprature=float(input('enter a temperature in Celsius'))

if temprature < -273.15:
    print('the temperature is invalid because it is below absolute zero.')
elif temprature == -273.15:
    print('the temperature is absolute 0.')
elif temprature > -273.5 and temprature < 0:
    print('temperature is below freezing.')
elif temprature == 0:
    print('the temperature is at the freezing point.')
elif temprature > 0 and temprature < 100:
    print('the temperature is in the normal range.')
elif temprature == 100:
    print('the temperature is at the boiling point.')
elif temprature > 100:
    print('temperature is above the boiling point.')
else:
    print('something went wrong!!!')
