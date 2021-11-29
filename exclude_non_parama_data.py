# -*- coding: utf-8 -*-
# +
import json
output_status = 1 #出力の変更：0が正解ラベル, 1がデータセット出力

###変更部分####
relate_data_file_path = "/data/ap_data/relate_only_dataset/01_c_test.txt"
dataset_path = "/data/kddi/data/01/test-data/network-5gc-c/"
##############

#初期値設定
label = 0 #初期ラベル：常にnormalスタート
udm_in_oct_pre = 0
amf_in_oct_pre = 0
ausf_in_oct_pre = 0
udm_out_oct_pre = 0
amf_out_oct_pre = 0
ausf_out_oct_pre = 0

with open(relate_data_file_path, "r", encoding="utf_8") as f:
    while True:
        line = f.readline() # 1行ずつ読み込み
        if line:#行が残っていれば繰り返す
            if len(line.split(',')) == 1:
                line = line.replace( '\n' , '')
                with open(dataset_path + line, "r", encoding="utf_8") as f_data:
                    jsn = json.load(f_data)
                    #udm系
                    try:
                        c0_usr_udm = jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user']#core0のuser
                    except TypeError as e:
                        print(line)
                    try:
                        str_casca = jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"]
                    except TypeError as e:
                        print(line)
                    try:
                        str_casca = jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"]
                    except TypeError as e:
                        print(line)
                    try:
                        str_casca = jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"]
                    except TypeError as e:
                        print(line)
        else:
            break
print("終了")
# -


