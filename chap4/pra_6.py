# welcome to the chapter 4 practical 6


item=int(input(' how many items you are buying'))

if item < 10:
    print('charges $12 per item that is $',item*12)
elif item >= 10 and item <= 99:
    print('charges $10 per item that is $',item*10)
elif item >= 100:
    print('charges $7 per item that is $',item*7)
else:
    print('Invalid Entry!!!!')



