def temp_convertor(isCtoF, input_value):
    if isCtoF == "Yes":
        output_value = (input_value * 1.8) + 32
    else:
        output_value = (input_value - 32) / 1.8
    return output_value
user_input = float(input("Enter the temperature: "))
isC = input("Is the value in \celsius? Type Yes or No: ")
print("Converted value is : ", temp_convertor(isC, user_input))
