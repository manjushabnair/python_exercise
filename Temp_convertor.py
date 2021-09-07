def temp_convertor(isCtoF, input_value):
    if isCtoF == True:
        output_value = (input_value * 1.8) + 32
    else:
        output_value = (input_value - 32) / 1.8
    return output_value

print(temp_convertor(False, 100.4))
