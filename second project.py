weight = float(input("ENTER YOUR WEIGHT IN KILOGRAMS :"))

height = float(input("ENTER YOUR HEIGHT IN METERS: "))

#bmi calculation

BMI = weight/(height**2)

if BMI <18.5:
    iterpretation = "UNDERWEIGHT"
elif BMI>=18.5 and BMI<25:
    interpretation = "NORMAL WEIGHT"
elif BMI>25 and BMI<30:
    interpretation = "OVERWEIGHT"
else:
    interpretation = "OBESE"

print("YOUR BMI IS :",BMI)
print("INTERPRETAION:",interpretation)
