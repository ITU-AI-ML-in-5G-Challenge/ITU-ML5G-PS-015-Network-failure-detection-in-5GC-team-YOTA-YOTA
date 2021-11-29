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

for num in range(6):
    select_data = num

    if select_data == 0:
        label_path = "/data/kddi/data/01/training-data/failure-label-a"
        data_path = "/data/kddi/data/01/training-data/network-5gc-a"
    elif select_data == 1:
        label_path = "/data/kddi/data/01/test-data/failure-label-a"
        data_path = "/data/kddi/data/01/test-data/network-5gc-a"
    elif select_data == 2:
        label_path = "/data/kddi/data/01/training-data/failure-label-c"
        data_path = "/data/kddi/data/01/training-data/network-5gc-c"
    elif select_data == 3:
        label_path = "/data/kddi/data/01/test-data/failure-label-c"
        data_path = "/data/kddi/data/01/test-data/network-5gc-c"
    elif select_data == 4:
        label_path = "/data/kddi/data/02/training-data/failure-label-b"
        data_path = "/data/kddi/data/02/training-data/network-5gc-b"
    elif select_data == 5:
        label_path = "/data/kddi/data/02/test-data/failure-label-b"
        data_path = "/data/kddi/data/02/test-data/network-5gc-b"
    else:
        print("正しくないデータの選択")
        exit()
        
    print("pass：{}".format(label_path))

    #正解ラベルの取得
    files_label = glob.glob(label_path + "/*")
    files_label.sort() #絶対パスで格納
    f_type = []

    #データファイルの取得
    # files_data = glob.glob(data_path + "/*")
    # files_data.sort() #絶対パスで格納

    # index = 0 #正解ラベルのインデックス
    # max_index = len(files_label) #例外処理用の正解ラベル最大値

    #正解とデータの時間関係を表示
    for i_file in range(len(files_label)):
        with open(files_label[i_file]) as f:
            jsn = json.load(f)
            label_f_name = files_label[i_file].rsplit('/',1)[1]
            if jsn['failure_type']=="normal":
                print('file:{} , f_type:{}'.format(label_f_name,jsn['failure_type']))
            else:
                print('file:{} , f_type:{} , f_location:{}'.format(label_f_name,jsn['failure_type'],jsn['node']))

# -


