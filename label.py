# +
import glob
import json
import pprint

data_path = "/data/kddi/data/01/training-data/failure-label-a"
files = glob.glob(data_path + "/*")
files.sort()
f_type = []

for file in files:
    with open(file) as f:
        jsn = json.load(f)
        print('%s : %s' % (file , jsn["failure_type"]))
        f_type.append(jsn["failure_type"])

"""
dict_f_type = {}
list_f_type = []

for failure_type in f_type:
    if (failure_type in list_f_type) == True:
        f_num = int(dict_f_type[failure_type])
        f_num = f_num + 1
        dict_f_type[failure_type] = f_num
    else:
        dict_f_type[failure_type] = 1
        list_f_type.append(failure_type)
        
pprint.pprint(dict_f_type)
"""
# -


