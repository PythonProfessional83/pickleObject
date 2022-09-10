# unpickling.py
'''
Unpicling the object from the file and from the file with pickled dictionary {manufacturer:object}.
Playing with files.
'''
import pickle
import os
from pathlib import Path

# changing current directory
os.chdir(Path.cwd() / Path('Pickle object'))
print('\n', Path.cwd())


def main():
    #
    #
    # unpickle object from dictionary {manufacturer:object}
    #
    inputFile = open('cellphoneDict.dat', 'rb')
    phoneDict = pickle.load(inputFile)

    print(f"\nphoneDict: {phoneDict}")

    for key, phone in phoneDict.items():
        print(f"key: {key}")
        print(f"manufacturer: {phone.manufacturer}")
        print(f"model: {phone.model}")
        print(f"price: {phone.price}\n")

    #
    #
    # unpickle object from file
    #

    # playig with files - extracting all files .dat - 1st method
    datFiles = os.listdir(Path.cwd())
    print(f"os.listdir(Path.cwd()):\n{os.listdir(Path.cwd())}\n")

    files = []
    for file in os.listdir(Path.cwd()):
        if file.endswith('.dat'):
            files.append(file)

    print(f"\ndatFiles:{files}")

    # 2nd method - extracting .dat files
    datFiles = Path.cwd().glob('*,dat')  # genetator object
    print(f"list(Path.cwd().glob('*.dat')):\n{list(Path.cwd().glob('*.dat'))}")
    print(
        f"\nPath.cwd().glob('*,dat')\n{[os.path.basename(fileName) for fileName in list(Path.cwd().glob('*.dat'))]}")

    fileDict, fileObject = [os.path.basename(
        fileName) for fileName in list(Path.cwd().glob('*.dat'))]
    print(f"\nfileObject: {fileObject}")

    #
    #
    # extracting object's data from the file with objects - object is not iterable!
    #
    inputFile = open(fileObject, 'rb')
    endOfFile = False

    c = 0
    while not endOfFile:
        try:
            c += 1
            print(f"\nLoading object{c}:")

            # extracting object from the file.dat
            objecT = pickle.load(inputFile)

            print(f"objecT.manufacturer: {objecT.manufacturer}")
            print(f"objecT.model: {objecT.model}")
            print(f"objecT.price: {objecT.price}")
        except EOFError:  # coming to the end of the file.dat
            endOfFile = True  # finish the loop


main()

'''
out:
(base) xxxxxxx@Xxxxxxx OOP % python -u "/Users/xxxxxxx/Python projects/Python Projects/Projects1/OOP/Pickle object/unpickling.py"

 /Users/xxxxxxx/Python projects/Python Projects/Projects1/OOP/Pickle object

phoneDict: {'nokia': <cellphone.Cellphone object at 0x7fc9c01c8f40>, 'sony': <cellphone.Cellphone object at 0x7fc9c01c8ee0>, 'xioami': <cellphone.Cellphone object at 0x7fc9a007e3d0>}
key: nokia
manufacturer: nokia
model: nk234
price: 23.45

key: sony
manufacturer: sony
model: sn345
price: 23.45

key: xioami
manufacturer: xioami
model: xi345
price: 342.0

os.listdir(Path.cwd()):
['unpickling.py', '__pycache__', 'README.md', 'cellphone.py', 'cellphoneDict.dat', 'pickling.py', 'cellphone.dat']


datFiles:['cellphoneDict.dat', 'cellphone.dat']
list(Path.cwd().glob('*.dat')):
[PosixPath('/Users/xxxxxxx/Python projects/Python Projects/Projects1/OOP/Pickle object/cellphoneDict.dat'), PosixPath('/Users/xxxxxxx/Python projects/Python Projects/Projects1/OOP/Pickle object/cellphone.dat')]

Path.cwd().glob('*,dat')
['cellphoneDict.dat', 'cellphone.dat']

fileObject: cellphone.dat

Loading object1:
objecT.manufacturer: xioami
objecT.model: xi345
objecT.price: 342.0

Loading object2:
objecT.manufacturer: nokia
objecT.model: nk234
objecT.price: 34.34

Loading object3:
objecT.manufacturer: sony
objecT.model: sn345
objecT.price: 23.33

Loading object4:
objecT.manufacturer: xaiomi
objecT.model: xi345
objecT.price: 55.4

Loading object5:

'''
