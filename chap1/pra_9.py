# welcome to the chapter 1 practical 9


price_of_meal=float(input('Enter your meal price'))

per_tip=float(input('Enter tip you have to give :'))

tip_amount=per_tip/100*price_of_meal

print('Meal price :',price_of_meal,' ',per_tip,'%','tip amount :',tip_amount,'Total amount with tip',price_of_meal+tip_amount)
