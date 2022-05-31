#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

def num (a):
    list=[]
    for i in range(0,a):
        list.append((-3)**i)
    print(list)
num (5) 


#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]
def num (a):
    num=1
    for i in range(1,a+1):
        num = num*i
        print(num)
num (4)


#Подсчитать сумму цифр в вещественном числе.

num= input("Введите вещественное число: ")
num1 = num.split(".") 
intnum=int(num1[0])
digitnum=int(num1[1])
sum=0
while intnum>0:
    sum=sum+(intnum%10)
    intnum=intnum//10
while digitnum>0:
    sum=sum+(digitnum%10)
    digitnum=digitnum//10
print(sum)