# -*- coding: utf-8 -*-
# +
import glob
import json
import pprint

data_path = "/data/kddi/data/01/training-data/network-5gc-a/20210128174620.json"

with open(data_path) as f:
    jsn = json.load(f)
#     pprint.pprint(jsn["gnb"][1]['software-oper']['cisco-platform-software']['control-processes']['control-process'])
    print(jsn["ausf"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]["used-percent"])
    print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
    
    #memory-stats
    #udma1: jsn["udm"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]['memory-status']
    #amfa1: jsn["amf"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]['memory-status']
    #ausfa1: jsn["ausf"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]['memory-status']
    
    #"used-percent"
    #udma1: jsn["udm"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]['"used-percent"]
    #amfa1: jsn["amf"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]['"used-percent"]
    #ausfa1: jsn["ausf"][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]["memory-stats"]['"used-percent"]
    
# -
# # udma1の確認、ens4のinocted、out-octが怪しい
# #         json_val = int(jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][4]["statistics"]["in-octets"]) - pre_val
# #         pre_val = int(jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][4]["statistics"]["in-octets"])
#         # amfa1の確認、ens4のinocted、out-octが怪しい
#         json_val = int(jsn_data["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"]) - pre_val
#         pre_val = int(jsn_data["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])
#         
#         print('{}:{},'.format(data_f_name , str(json_val)))
#                               #jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][1]["statistics"]["in-octets"]))
#                               #jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["speed"])) #inter-downのspeed
# #                               jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"])) # inter-downのoper-status

