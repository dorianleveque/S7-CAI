# import cPickle as pickle
import json
with open("signal.json","r") as f:
#    signal=pickle.load(f)
    signal=json.load(f)
print(signal)
