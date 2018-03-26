import pickle
result = dict()

print(dict.items)
print()
# сохраняем словарь в файл
with open('dump.dat', 'wb') as dump_out:
    pickle.dump(result, dump_out)

# загружаем словарь из файла
with open('dump.dat', 'rb') as dump_in:
    der = pickle.load(dump_in)

for key, value in der.items():
    print(key, value)

# обновляем словарь
result = dict(NESKWI = '166965975', DarkDenisssimo='505269223')

# снова сохраняем словарь в файл
with open('dump.dat', 'wb') as dump_out:
    pickle.dump(result, dump_out)

# снова загружаем словарь из файла
with open('dump.dat', 'rb') as dump_in:
    der = pickle.load(dump_in)

for key, value in der.items():
    print(key, value)