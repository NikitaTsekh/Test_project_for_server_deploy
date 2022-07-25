import pathlib
import pickle
import os
from random import randrange


# Press the green button in the gutter to run the script.
from datetime import date

if __name__ == '__main__':
    print(pathlib.Path.home())
    path='/home/mluser/Model_building'

    #path='/home/mluser/Model_building'
    # os.chdir(path)
    # print(pathlib.Path.home())
    # print(pathlib.Paths().resolve())

    list1=[1,2,3,4,5]
    print(list1)

    numb=(randrange(100))
    current_date = date.today()

    # with open(os.path.join(path,f"serialized_data/list_{str(numb)}.pkl"), "wb") as f:
    #     pickle.dump(list1, f)
    print(numb)
