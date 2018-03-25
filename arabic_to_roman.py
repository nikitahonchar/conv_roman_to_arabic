
#Перевод чисел с арабских в римские

#Словарь арабских и римских чисел
numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
letters = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

def arabic_to_roman():
    rom = ''    #начальное значение римского числа
    j=0         #начальное значение счетчика для елементов словаря
    arab = int(input("Введите Арабское число: "))
    while arab > 0:           
        if arab >= numbers[j]:
            rom += letters[j]       
            arab -= numbers[j]    
        else: j += 1

    print('Римское число: ', rom)

arabic_to_roman()
