import pickle

a =open('22.zip','rb').read()

with open('filename.sas', 'wb') as handle:
  pickle.dump(a, handle)

with open('filename.sas', 'rb') as handle:
  b = pickle.load(handle)

