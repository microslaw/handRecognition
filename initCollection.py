import pickle
from os import mkdir

mkdir("data")
with open("data/count.pickle", "wb") as savePickle:
    pickle.dump(0, savePickle)
