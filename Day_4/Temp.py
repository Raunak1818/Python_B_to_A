unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter your temperature: "))

        #    F = (C x 9/5) + 32 
if unit == "C":
    temp = (9 * temp ) / 5 + 32
    print(f"The temperature in Fahrenheit is : {temp} F")
  
        #   C = (F - 32) x 5/9
elif unit == "F":
    temp = ((temp - 32) * 5/9)
    print(f"The temperature in Celcius is : {temp} C")

else:
    print(f"{unit} is an invalid unit of a measurement.")






