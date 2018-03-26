import pickle
with open('dump.dat', 'rb') as dump_in:
    der = pickle.load(dump_in)

for key, value in der.items():
    print(key, value)