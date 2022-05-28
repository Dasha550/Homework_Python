#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4

import numbers

sum=0
numbers = [1, 2, 3, 4]
even_index = [x for x in numbers if x%2]
for i in range(len(even_index)):
    sum=sum+even_index[i]

print(sum)
