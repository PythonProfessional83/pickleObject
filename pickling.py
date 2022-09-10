# pickling.py
'''
Serializing the object and dictionary with the object to the file.
'''
from pathlib import Path
import os
import pickle
import cellphone

# preparing the directory
os.chdir(Path.cwd()/Path('Pickle object'))
print('Path.cwd(): ', Path.cwd())

yes = 'y'
FILENAME1 = 'cellphone.dat'
FILENAME2 = 'cellphoneDict.dat'

# creating dictionary with the object
phoneDict = {}

while yes == 'y':
    man = input(f"\n\nEnter manufacturer: ")
    model = input('Enter model: ')
    price = float(input('Enter the price: '))

    # object
    cellPhone = cellphone.Cellphone(man, model, price)

    # object to the dictionary
    # if next manufacturer key value is the same, object will be overrided
    phoneDict[man] = cellPhone

    yes = input(
        "\nIf you want to enter next phone data press 'y' or any other to finish: ")

    # saving the object to the file
    filE = open(FILENAME1, 'ab')
    # always new one object is the same
    pickle.dump(cellPhone, filE)
    filE.close()

    # saving the dictionary with object to the file
    file = open(FILENAME2, 'ab')
    # saving dictionery: newe objects overriding the old one, when the key value is the same
    pickle.dump(phoneDict, file)
