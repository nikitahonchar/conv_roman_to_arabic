#Перевод чисел с римских в арабские

#Словарь арабских и римских чисел
num_arab = [1000,500,100,50,10,5,1]
num_rom = ["M","D","C","L","X","V","I"]

def roman_to_arabic():
    arabic = 0  #начальное значение арабского числа
    roman = input("Введите Римское число: ")

    # Cуммируем значение всех цифр введенного числа
    for i in range(len(roman)):
        letter = roman[i]
        for j in range(len(num_rom)):
            if letter == num_rom[j]:
                arabic += num_arab[j]

    # Делаем двойные вычитания, эквивалентно римскому значению
    for i in range(1, len(roman)):
        letter = roman[i]
        if (letter == "M" or letter == "D") and roman[i-1] == "C":      #если перед "М" или "D" стоит "С" вычитаем 100*2
            arabic -= 200
        elif (letter == "C" or letter == "L") and roman[i-1] == "X":    #если перед "С" или "L" стоит "X" вычитаем 10*2
            arabic -=20
        elif (letter == "X" or letter == "V") and roman[i-1] == "I":    #если перед "X" или "V" стоит "I" вычитаем 1*2
            arabic -= 2

    print('Арабское число: ', arabic)

roman_to_arabic()