grade = 88
if grade >= 90:
     print('Excellent')
elif grade >= 80:
    print('Very good')
elif grade >= 70:
    print('Good')
else:
    print('Not good')

# Exercise

age = int(input("Enter your age: "))

if age < 13:
    print("Children!! Your ticket will cost shs1000")
elif age in range(13, 19):
    print("Teenagers!! Your ticket will cost shs500")
elif age >= 18 and age < 65:
    print("Adults!! Your ticket will cost shs2000")
else:
    print("Senior citizens!! Your ticket will cost shs5000")
    
#Example 3

cars = ['Tesla', 'Audi', 'BMW', 'Jeep','RangeRover']
for car in cars:
    print(car)
    
# Example 4 count 1 to 10
count = 1
while count <=5:
    print("Count 1 to 10:", count)
    count += 1
    
#Exercise 2
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
for color in colors:
    print(color)

#Exercise 3
count = 5
while count >= 1:
    print(count)
    count -= 1