# import cPickle as pickle
import json
signal=[1,2,3]
with open("signal.json","w") as f:
#    pickle.dump(signal,f)
    json.dump(signal,f)

