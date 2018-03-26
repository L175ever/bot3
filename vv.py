import pickle
result = dict()

print(dict.items)
print()
# сохраняем словарь в файл
with open('dump.dat', 'wb') as dump_out:
    pickle.dump(result, dump_out)