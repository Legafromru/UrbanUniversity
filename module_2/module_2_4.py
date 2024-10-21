numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
'''Используя этот список составьте: 
    второй список primes содержащий только простые числа.
    третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:'''
primes = [] #Создайте пустые списки primes и not_primes.
not_primes = []
for i in numbers: #При помощи цикла for переберите список numbers.
    if i/2==1 or i/3==1:  #отсеиваем числа 2 и 3
        primes.append(i)
    for j in range (3, i, 2): #Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1 цикла.
        if i % j == 0 or i % 2 == 0:
            not_primes.append(i)
            break
        else:
            primes.append(i)
            break
print('primes :', primes)
print('not_primes :', not_primes)

#Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
#В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
#Выведите списки primes и not_primes на экран(в консоль).