#Написать программу преобразования десятичного числа в двоичное

numbers_decimal = 10
 
numbers_binary = ''
 
while numbers_decimal > 0:
    numbers_binary = str(numbers_decimal % 2) + numbers_binary
    numbers_decimal = numbers_decimal // 2
 
print(numbers_binary)