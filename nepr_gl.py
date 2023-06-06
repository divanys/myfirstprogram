import random

list1 = ['major computing company', 'take a decision', 'get out of the busineness', 'believed', 'reversed their decision', 
         'set up a special team', 'go on sale', 'challenged', 'manufacturer', 'commodity items',
          'funded', 'initial rescarch', 'however', 'exating available electrical companents', 'badge', 'burchase',
           'turned to', 'development', 'consitered', 'endorsement', 'expandable']
list2 = ["крупная компьютерная компания", "принять решение", "выйти из бизнеса", "поверили", "отменили свое решение",
    "создали специальную команду", "поступили в продажу", "оспаривается", "производитель", "товарные позиции",
    "финансируется", "первоначальная повторная архивация", "однако", "существующие доступные электрические компоненты", "значок", "покупка",
    "обращено к", "разработка", "рассмотрено", "одобрение", "возможность расширения"]

# for i in range(50):
#     print(i)
#     rnd = random.randint(0, (len(list1) - 1))
#     print(f'{rnd}')
#     print(list1[rnd])
#     print('перевод слова на английский. ')
#     c = input()
for i in range(len(list2)):
    if input() == '':
        print(list1[i], ':', list2[i])
