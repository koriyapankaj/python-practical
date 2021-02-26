# welcome to the chapter 4 practical 2

temprature=float(input('Enter temprature :'))
flag=input('choose : (1) Celsius or (2) Fahrenheit').upper()

print(flag)

if flag == '1' or flag == 'CELSIUS' or flag == 'C':
    print(temprature,'celsius into fehrenheit',(9/5)*temprature+32)
elif flag == '2' or flag == 'FEHRENHEIT' or flag == 'F':
    print(temprature,'fehrenheit into celsius',5/9*(temprature-32))
else:
    print('invalid entry !!!')



