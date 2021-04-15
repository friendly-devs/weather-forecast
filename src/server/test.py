from random import Random

ran = Random(42)
weathers = ['Mua', 'Mua nhe', 'Nang', 'Nang nhe']

with open('weathers.txt', 'w') as file:
    for i in range(1, 5):
        file.write('{}'.format(i))
        for j in range(0, 6):
            file.write(', {}'.format(weathers[ran.randint(0, 3)]))
            min = ran.randint(25, 34)
            file.write(', {}'.format(min))
            file.write(', {}'.format(min + ran.randint(3, 10)))
        file.write('\n')
