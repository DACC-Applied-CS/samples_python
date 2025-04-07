##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

import pickle
my_list = ['Marshall','Anthony','Brayden']
print(my_list)

with open('names.bin','wb') as file:
    pickle.dump(my_list, file)

new_list = []
print("New list to start is", new_list)

with open('names.bin','rb') as file:
    new_list = pickle.load(file)
    print("New list now is", new_list)

print()
