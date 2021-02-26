# welcome to the chapter 2 practical 11

height=int(input('Enter BOX height :'))
width=int(input('Enter BOX width :'))

print('*'*width)
for i in range(height-2):
    print('*',' '*(width-2),'*')
print('*'*width)
