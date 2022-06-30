# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
#  It’s calculated using a person's weight and height, using this formula: weight / height²
Height = float (input("Enter Your Height In Centemeter : "))
Weight = float(input("Enter Your Weight in Kg: "))

Height =Height/100
# calling the BMI function
BMI = Weight/(Height*Height)

print ("Your Body Mass Index is:",BMI)
# Conditions to find out BMI category
if(BMI>0):
    if(BMI<=16):
        print("you are Severely Underweight")
    elif (BMI<=18.5):
        print("you are Underweight")
    elif (BMI<=25):
        print("You are Healthy")
    elif (BMI<=30):
        print ("you are overweight")
    else:
        print("you are severely overweight")
else:
    print ("Enter valid details...")          