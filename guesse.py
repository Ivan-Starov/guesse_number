from random import randint


number = randint(1, 100)
print('Угадайте число от 1 до 100')   

while True:

    text = int(input('Введите ваше число: '))

    if text > number:
        print('Ваше число больше загаданного')
    if text < number:
        print('Ваше число меньше загаданного')    
    if text == number:
        print('Вы угадали, у вас прекрасная интуиция!')    
        break
    
print('Игра завершена!')      
