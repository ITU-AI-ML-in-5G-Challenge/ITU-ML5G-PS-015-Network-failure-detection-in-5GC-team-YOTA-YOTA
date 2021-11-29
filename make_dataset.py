# -*- coding: utf-8 -*-
# +
import json

#####Select the data you want to output###########
#出力の変更(output)
#0:label
#1:dataset
output_status = 0
""
##############Please specify where the data is located.##########
relate_data_file_path = "/data/ap_data/relate_only_dataset/"
dataset_path = "/data/kddi/data/02/test-data/network-5gc-b/"
output_file_name = "02_b_test.txt"
""


#初期値設定
label = 0 #初期ラベル：常にnormalスタート
udm_in_oct_pre = 0
amf_in_oct_pre = 0
ausf_in_oct_pre = 0
udm_out_oct_pre = 0
amf_out_oct_pre = 0
ausf_out_oct_pre = 0

#ラベルの付け方
"""
0:normal
1:bridge-delif系
2:interface-down系
3:interface-loss-start系
4:memory-stress-start系
5:vcpu-overload-start系
"""

with open(relate_data_file_path + output_file_name, "r", encoding="utf_8") as f:
    while True:
        line = f.readline() # 1行ずつ読み込み
        if line:#行が残っていれば繰り返す
            if len(line.split(',')) == 1:
                if output_status == 0: #正解ラベルの出力
                    print(str(label))
                elif output_status == 1: #データセットの出力
                    line = line.replace( '\n' , '')
#                     print(line)
                    with open(dataset_path + line, "r", encoding="utf_8") as f_data:
                        jsn = json.load(f_data)
                        
                        ############interface_down(山口)##############
                        #udmのoper_status
                        if jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"] == "up":
                            udm_oper_status = 0
                        elif jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"] == "down":
                            udm_oper_status = 1
                            
                        #amfのoper_status
                        if jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"] == "up":
                            amf_oper_status = 0
                        elif jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"] == "down":
                            amf_oper_status = 1
                            
                        #ausfのoper_status
                        if jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"] == "up":
                            ausf_oper_status = 0
                        elif jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"] == "down":
                            ausf_oper_status = 1
                        
                        ############bridge_delif(山口)##############
                        #udm系
                        udm_in_oct = int(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"]) - udm_in_oct_pre #in-octets
                        udm_in_oct_pre = int(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])
                        
                        #amf系
                        amf_in_oct = int(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"]) - amf_in_oct_pre#in-octets
                        amf_in_oct_pre = int(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])
                        
                        #ausf系
                        ausf_in_oct = int(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"]) - ausf_in_oct_pre#in-octets
                        ausf_in_oct_pre = int(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])#in-octets
                        
                        
                        ############interface_loss(秋吉)##############
                        #udm系
                        udm_out_oct = int(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"]) - udm_out_oct_pre #out-octets
                        udm_out_oct_pre = int(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"])
                        
                        #amf系
                        amf_out_oct = int(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"]) - amf_out_oct_pre#out-octets
                        amf_out_oct_pre = int(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"])
                        
                        #ausf系
                        ausf_out_oct = int(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"]) - ausf_out_oct_pre#out-octets
                        ausf_out_oct_pre = int(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"])
                        
                        
                        ############vcpu_overload(田代)##############
                        #udm系
                        c0_usr_udm = jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user']#core0のuser
                        c0_sys_udm = jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['system']#core0のsystem
                        c0_idle_udm = float(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['idle']) / 100 #core0のidle
                        c1_usr_udm = jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['user']#core1のuser
                        c1_sys_udm = jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['system']#core1のsystem
                        c1_idle_udm = float(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['idle']) / 100#core1のidle

                        #amf系
                        c0_usr_amf = jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user']#core0のuser
                        c0_sys_amf = jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['system']#core0のsystem
                        c0_idle_amf = float(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['idle']) / 100#core0のidle
                        c1_usr_amf = jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['user']#core1のuser
                        c1_sys_amf = jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['system']#core1のsystem
                        c1_idle_amf = float(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['idle']) / 100#core1のidle

                        #ausf系
                        c0_usr_ausf = jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user']#core0のuser
                        c0_sys_ausf = jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['system']#core0のsystem
                        c0_idle_ausf = float(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['idle']) / 100#core0のidle
                        c1_usr_ausf = jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['user']#core1のuser
                        c1_sys_ausf = jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['system']#core1のsystem
                        c1_idle_ausf = float(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['idle']) / 100#core1のidle
                        #c0_usr_ausf, c0_sys_ausf, c0_idle_ausf, c1_usr_ausf, c1_sys_ausf, c1_idle_ausf
                        
                        ############memory_stress(大嶋)##############
                        #udm系
                        if jsn['udm'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'] == "Healthy": #memory-status
                            mem_status_udm = 0
                        elif jsn['udm'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'] == "Critical":
                            mem_status_udm = 1
                        used_percent_udm = float(jsn['udm'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['used-percent']) / 100#used-percent
                        #amf系
                        if jsn['amf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'] == "Healthy": #memory-status
                            mem_status_amf = 0
                        elif jsn['amf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'] == "Critical":
                            mem_status_amf = 1
                        used_percent_amf = float(jsn['amf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['used-percent']) / 100#used-percent
                        #ausf系
                        if jsn['ausf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'] == "Healthy": #memory-status
                            mem_status_ausf = 0
                        elif jsn['ausf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'] == "Critical":
                            mem_status_ausf = 1
                        used_percent_ausf = float(jsn['ausf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['used-percent']) / 100#used-percent
                        #mem_status_udm, used_percent_udm, mem_status_amf, used_percent_amf, mem_status_ausf, used_percent_ausf
                        
                    #strでキャストしないといけないものもある
                    print(udm_oper_status, amf_oper_status, ausf_oper_status, udm_in_oct, amf_in_oct, ausf_in_oct, udm_out_oct, amf_out_oct, ausf_out_oct,c0_usr_udm, c0_sys_udm, c0_idle_udm, c1_usr_udm, c1_sys_udm, c1_idle_udm, c0_usr_amf, c0_sys_amf, c0_idle_amf, c1_usr_amf, c1_sys_amf, c1_idle_amf, c0_usr_ausf, c0_sys_ausf, c0_idle_ausf, c1_usr_ausf, c1_sys_ausf, c1_idle_ausf, mem_status_udm, used_percent_udm, mem_status_amf, used_percent_amf, mem_status_ausf, used_percent_ausf)
            
            elif len(line.split(',')) == 2:
                f_str = line.split(',')[1] #正解ラベルの種類保存
                if f_str == "bridge-delif\n": 
                    label = 1
                elif f_str == "interface-down\n": 
                    label = 2
                elif f_str == "interface-loss-start\n": 
                    label = 3
                elif f_str == "memory-stress-start\n": 
                    label = 4
                elif f_str == "vcpu-overload-start\n": 
                    label = 5
                elif (f_str == "bridge-addif\n") or (f_str == "interface-up\n") or (f_str == "interface-loss-stop\n") or (f_str == "memory-stress-stop\n") or (f_str == "vcpu-overload-stop\n") or (f_str == "normal\n"): 
                    label = 0                
            else:
                print("error : file is broken")
        else:
            break
# +
# import glob
# import json
# import pprint

# data_path = "/data/kddi/data/01/training-data/network-5gc-a/20210128174620.json"

# with open(data_path) as f:
#     jsn = json.load(f)
#     #pprint.pprint(jsn["gnb"][1]['software-oper']['cisco-platform-software']['control-processes']['control-process'])
#     #print(jsn["udm"][0].keys())
#     #print(jsn["udm"][0].keys())
    
#    #interface_down(山口)
#     print("interface_down")
#     #udm系
#     print(jsn["udm"][0]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])#名前
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"])#oper-status
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["speed"])#speed
#     print()
#     #amf系
#     print(jsn["amf"][0]["name"])
#     print(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"])#oper-status
#     print(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["speed"])#speed
#     print()
#     #ausf系
#     print(jsn["ausf"][0]["name"])
#     print(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["oper-status"])#oper-status
#     print(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["speed"])#speed
#     print()
    
#    #bridge_delif(山口)
#     print("bridge_delif")
#     #udm系
#     print(jsn["udm"][0]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])#in-octets
#     print()
#     #amf系
#     print(jsn["amf"][0]["name"])
#     print(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])#in-octets
#     print()
#     #ausf系
#     print(jsn["ausf"][0]["name"])
#     print(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["in-octets"])#in-octets
#     print()
    
    
#   #interface_down(秋吉)
#     print("interface_down")
#     #udm系
#     print(jsn["udm"][0]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"])#out-octets
#     print()
#     #amf系
#     print(jsn["amf"][0]["name"])
#     print(jsn["amf"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"])#out-octets
#     print()
#     #ausf系
#     print(jsn["ausf"][0]["name"])
#     print(jsn["ausf"][0]["interfaces"]['interfaces-state']['interface'][2]["name"])
#     print(jsn["udm"][0]["interfaces"]['interfaces-state']['interface'][2]["statistics"]["out-octets"])#out-octets
#     print()
    
#    #vcpu_overload(田代)
#     print("vcpu_overload")
#     #udm系
#     print(jsn["udm"][0]["name"])
#     print(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user'])#core0のuser
#     print(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['system'])#core0のsystem
#     print(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['idle'])#core0のidle
#     print(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['user'])#core1のuser
#     print(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['system'])#core1のsystem
#     print(jsn["udm"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['idle'])#core1のidle
#     print()
#     #amf系
#     print(jsn["amf"][0]["name"])
#     print(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user'])#core0のuser
#     print(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['system'])#core0のsystem
#     print(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['idle'])#core0のidle
#     print(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['user'])#core1のuser
#     print(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['system'])#core1のsystem
#     print(jsn["amf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['idle'])#core1のidle
#     print()
#     #ausf系
#     print(jsn["ausf"][0]["name"])
#     print(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['user'])#core0のuser
#     print(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['system'])#core0のsystem
#     print(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][0]['idle'])#core0のidle
#     print(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['user'])#core1のuser
#     print(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['system'])#core1のsystem
#     print(jsn["ausf"][0]["software-oper"]['cisco-platform-software']['control-processes']['control-process'][0]['per-core-stats']['per-core-stat'][1]['idle'])#core1のidle
#     print()

    
#    #memory_stress(大嶋)
#     print("memory_stress")
#     #udm系
#     print(jsn['udm'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'])#memory-status
#     print(jsn['udm'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['used-percent'])#used-percent
#     #amf系
#     print(jsn['amf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'])#memory-status
#     print(jsn['amf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['used-percent'])#used-percent
#     #ausf系
#     print(jsn['ausf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['memory-status'])#memory-status
#     print(jsn['ausf'][0]['software-oper']['cisco-platform-software']['control-processes']['control-process'][0]['memory-stats']['used-percent'])#used-percent
# -



