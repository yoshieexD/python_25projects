# x = 1
# y = 2.5
# name = 'John'
# is_cool = True

#multiple assignment 
x,y,name,is_cool = (1,2.5,'john',True)

#print Hello
print(x,y,name,is_cool)

#checking type
print(type(x))

#return to string
x =str(x)
print(type(x))

#return to int
x = int(x)
print(type(x))
#return to float 
y = float(y)
print(type(y))
#printing the type also the x
print(type(x),x)

#concatenate 
names = 'Brad'
age = 37
age =str(age)
print('Hello, my name is ' + names + 'and i am ' + age)