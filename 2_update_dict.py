# Добавление и обновление элементов словаря
# 1)название_словаря[ключ]=значение
# 2) метод update()
#   название_словаря.update({ключ:значение})

region_codes={
    'Амурская область':[28],
    'Волгоградская область':[34,134],
    'Иркутская область':[38, 138, 85],
    'Костромская область':[44],
}
region_codes['Свердловская область']=[66,96,196]
region_codes.update({'Пермская область':[59,159]})
print(region_codes)