#В словаре приведены значения годовые объемы продаж автомобилей (в тысячах) в России

title = {'Некоммерческие':
             {'Универсалы':
                  {'Ауди A6': 3,'Вольво s60': 6},
              'Минивэны':
                  {'Киа Carnival': 4,'Toyota Heace' : 3},
              'Пикапы':
                  {'Volkswagen Amarok': 1,'Toyota Hillux' : 2 },
              'Седаны':
                  {'Lada Vesta': 495,'Hyundai Solaris': 211, 'Kia Rio': 314, 'Renault Logan': 128,'Toyota Camry': 12},
              'Кроссоверы':
                  {'Hyundai Creta': 128,'BMW x1': 12,'Toyota Rav4': 98,'Volkswagen Tiguan':102},
        'Коммерческие':
            {'Лада': 343,
             'Kia': 219,
             'Hyundai': 163,
             'Газ': 51,
             'Уаз': 36}
              }
         }


def stat(ttl,search):
    if search in ttl.keys():
        return ttl[search]
    #n - вложенный словарь
    for n in ttl.values():
        if type(n) == dict:
            if stat(n,search) != None:
                return stat(n,search)
search = input('Введите название автомобиля: ')
print(stat(title,search), 'тысяч')