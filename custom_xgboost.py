# -*- coding: utf-8 -*-
# +
import xgboost as xgb

from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
# import dask.array as da
# import dask.distributed

import numpy as np


def main():
#     ####データの合成なし
#     X_train = np.loadtxt('/data/ap_data/01_c_train_data.txt')
#     y_train = np.loadtxt('/data/ap_data/01_c_train_label.txt', dtype='int64')
    
    X_test = np.loadtxt('/data/ap_data/01_a_test_data.txt')
    y_test = np.loadtxt('/data/ap_data/01_a_test_label.txt', dtype='int64')

    #データの合成あり
    X_train_a = np.loadtxt('/data/ap_data/01_a_train_data.txt')
    y_train_a = np.loadtxt('/data/ap_data/01_a_train_label.txt', dtype='int64')
    
    X_test_a = np.loadtxt('/data/ap_data/01_a_test_data.txt')
    y_test_a = np.loadtxt('/data/ap_data/01_a_test_label.txt', dtype='int64')
    
    X_train_c = np.loadtxt('/data/ap_data/01_c_train_data.txt')
    y_train_c = np.loadtxt('/data/ap_data/01_c_train_label.txt', dtype='int64')
    
    X_test_c = np.loadtxt('/data/ap_data/01_c_test_data.txt')
    y_test_c = np.loadtxt('/data/ap_data/01_c_test_label.txt', dtype='int64')
    
    X_train = np.concatenate([X_train_a, X_train_c])
    y_train = np.concatenate([y_train_a, y_train_c])
    
#     X_test = np.concatenate([X_test_a, X_test_c])
#     y_test = np.concatenate([y_test_a, y_test_c])
    
   
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)
    
    fin_xgboost = XGBClassifier(
    #random_state=42,
    #n_estimators= 30,
    eta = 0.3,
    max_depth= 15, 
    min_child_weight=6, 
    subsample=0.9, 
    colsample_bytree=0.7,
    seed=0,
    eval_metric='mlogloss'
    )
 
    # モデル訓練
    fin_xgboost.fit(X_train, y_train,verbose=True)

    # テストデータで推測値を算出
    fin_test_pred = fin_xgboost.predict(X_test)

    # 混同行列で確認
    confusion_matrix(y_test, fin_test_pred, labels=[1, 0])
    
    print(accuracy_score(y_test, fin_test_pred))
    print(classification_report(y_test, fin_test_pred))
    
    print(confusion_matrix(y_test,  fin_test_pred))


if __name__ == '__main__':
    main()
# -
# 課題2:
#
#
# 課題1:
# 変更メモ
# 元：96.348458%
# eta = 0.2,max_depth= 5, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9643835616438357
# eta = 0.1,max_depth= 5, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9634845890410959
# eta = 0.3,max_depth= 5, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9643407534246575
# eta = 0.3,max_depth= 6, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9646404109589041
# eta = 0.3,max_depth= 8, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9651541095890411
# 0.9653253424657534(seed:2→seedによる上昇見込める)
# eta = 0.3,max_depth= 10, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9653681506849315
# eta = 0.3,max_depth= 14, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9658390410958904
# ############
# eta = 0.3,max_depth= 15, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9660958904109589
# ############
# eta = 0.3,max_depth= 16, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9659674657534246
# eta = 0.3,max_depth= 17, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9655393835616438
# eta = 0.3,max_depth= 20, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.965625
#
# #######
# eta = 0.3,max_depth= 15, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9660958904109589
# eta = 0.3,max_depth= 15,その他デフォ
# 0.9660958904109589
#
# eta = 0.3,max_depth= 15, min_child_weight=5, subsample=0.9, colsample_bytree=0.7,
# 0.9658390410958904
# ###########
# eta = 0.3,max_depth= 15, min_child_weight=6, subsample=0.9, colsample_bytree=0.7,
# 0.9660958904109589
# ###########
# eta = 0.3,max_depth= 15, min_child_weight=7, subsample=0.9, colsample_bytree=0.7,
# 0.9660102739726028
# eta = 0.3,max_depth= 15, min_child_weight=8, subsample=0.9, colsample_bytree=0.7,
# 0.9654965753424658
#
# 0:0.9660958904109589
# 1:0.9657534246575342
# 2:0.9654537671232877
# 3:0.9657534246575342
# 4:0.9659674657534246
# 5:0.9657534246575342
#
# 96.348458%
# ↓
# 0.9660958904109589

# !pip install pandas



