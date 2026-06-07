print("===== BMI CALCULATOR =====")

name = input("Enter Your Name: ")
weight = float(input("Enter Your Weight (kg): "))
height = float(input("Enter Your Height (m): "))

bmi = weight / (height ** 2)

print("\nName:", name)
print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\nThank You For Using BMI Calculator")