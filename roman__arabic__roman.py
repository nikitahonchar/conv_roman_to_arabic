
#Перевод чисел с римских в арабские и обратно

#Словарь арабских и римских чисел
num_arab = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
num_rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

def roman_to_arabic ():
    arabic = 0      #начальное значение арабского числа
    rom = ''        #начальное значение римского числа
    n = 0           #начальное значение счетчика для елементов словаря
    roman = input("Введите Римское число: ")
#Cуммируем значение всех цифр введенного числа
    for i in range(len(roman)):
        letter = roman[i]
        for j in range(len(num_rom)):
            if letter == num_rom[j]:
                arabic += num_arab[j]
#Делаем двойные вычитания, эквивалентно римскому значению
    for i in range(1, len(roman)):
        letter = roman[i]
        if (letter == "M" or letter == "D") and roman[i-1] == "C":      #если перед "М" или "D" стоит "С" вычитаем 100*2
            arabic -= 200
        elif (letter == "C" or letter == "L") and roman[i-1] == "X":    #если перед "С" или "L" стоит "X" вычитаем 10*2
            arabic -=20
        elif (letter == "X" or letter == "V") and roman[i-1] == "I":    #если перед "X" или "V" стоит "I" вычитаем 1*2
            arabic -= 2
#Подсчет с арабских в римские
    arab = arabic
    while arab > 0:             #выполняется, пока наше число не станет 0
        if arab >= num_arab[n]:
            rom += num_rom[n]   #добавляем значения в исходную переменную rom, эквивалентно арабскому
            arab -= num_arab[n] #соответсвенно уменьшаем наше число на выше добавленное
        else: n = n+1

    print('Арабское число: ', arabic)
    print('Римское: ', rom)

roman_to_arabic()