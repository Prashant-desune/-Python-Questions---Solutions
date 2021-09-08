#Q.8)# Python Program to convert temperature in celsius to fahrenheit and vice-versa
temperature = float(input("temp to convert::"))
fahrenheit = (temperature * 1.8) + 32
celsius = (temperature - 32) / 1.8
print('%0.2f'%fahrenheit)
print('%0.2f'%celsius)

