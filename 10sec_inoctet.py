# -*- coding: utf-8 -*-
# +
import glob
import json
import pprint

#データの選択
#1:01-aの訓練データ
#2:01-aのテスト用データ
#3:01-cの訓練データ
#4:01-cのテスト用データ
#5:02の訓練データ
#6:02のテスト用データ
select_data = 1

#################Change the path here to the path of your own data and the correct answer label.########

if select_data == 1:
    label_path = "/data/kddi/data/01/training-data/failure-label-a"
    data_path = "/data/kddi/data/01/training-data/network-5gc-a"
elif select_data == 2:
    label_path = "/data/kddi/data/01/test-data/failure-label-a"
    data_path = "/data/kddi/data/01/test-data/network-5gc-a"
elif select_data == 3:
    label_path = "/data/kddi/data/01/training-data/failure-label-c"
    data_path = "/data/kddi/data/01/training-data/network-5gc-c"
elif select_data == 4:
    label_path = "/data/kddi/data/01/test-data/failure-label-c"
    data_path = "/data/kddi/data/01/test-data/network-5gc-c"
elif select_data == 5:
    label_path = "/data/kddi/data/02/training-data/failure-label-b"
    data_path = "/data/kddi/data/02/training-data/network-5gc-b"
elif select_data == 6:
    label_path = "/data/kddi/data/02/test-data/failure-label-b"
    data_path = "/data/kddi/data/02/test-data/network-5gc-b"
else:
    print("正しくないデータの選択")
    exit()
    
##################################

#正解ラベルの取得
files_label = glob.glob(label_path + "/*")
files_label.sort() #絶対パスで格納
f_type = []

#データファイルの取得
files_data = glob.glob(data_path + "/*")
files_data.sort() #絶対パスで格納

index = 0 #正解ラベルのインデックス
max_index = len(files_label) #例外処理用の正解ラベル最大値

pre_val = 0#差分を表示するためのパラメータ

#正解とデータの時間関係を表示
for i_data in range(len(files_data)):
    data_f_name = files_data[i_data].rsplit('/',1)[1] #データファイルのパスから時間番号だけに加工
    data_time = int(data_f_name.rsplit('.',1)[0])
    if index < max_index:
        label_f_name = files_label[index].rsplit('/',1)[1]#正解ラベルファイルのパスから時間番号だけに加工
        label_time = int(label_f_name.rsplit('.',1)[0])
    
    if (label_time < data_time) & (index < max_index) :#正解ラベルの表示
        #print(label_path + '/' + label_f_name) #全てのラベル表示
        with open(label_path + '/' + label_f_name) as f:
            jsn = json.load(f)
#             if jsn["failure_type"]=="bridge-delif":# || (jsn["failure_type"]] == "bridge-addif"):
            if (jsn["failure_type"]=="bridge-delif") or (jsn["failure_type"] == "bridge-addif"):
                print(label_path + '/' + label_f_name) 
                print("#############", jsn["failure_type"], jsn["node"])
            #print('%s : %s' % (file , jsn["failure_type"]))
        index = index + 1
    
    with open(data_path + '/' + data_f_name) as f_data:
        jsn_data = json.load(f_data)
        
        # udma1の確認、ens4のinocted、out-octが怪しい
#         json_val = int(jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][4]["statistics"]["in-octets"]) - pre_val
#         pre_val = int(jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][4]["statistics"]["in-octets"])
        # amfa1の確認、ens4のinocted、out-octが怪しい
        json_val = int(jsn_data["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"]) - pre_val
        pre_val = int(jsn_data["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])
        
        print('{}:{},'.format(data_f_name , str(json_val)))
                              #jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][1]["statistics"]["in-octets"]))
                              #jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["speed"])) #inter-downのspeed
#                               jsn_data["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"])) # inter-downのoper-status
# #     print(data_f_name)#データの表示
    
print("ラベルの最後：" + files_label[len(files_label) - 1])
print("データの最後：" + files_data[len(files_data) - 1])
# -
# /data/kddi/data/01/training-data/network-5gc-aの終わり
# 20210215055410.json
# /data/kddi/data/01/training-data/failure-label-aの終わり
# 20210215054047.json



