# ITU-ML5G-PS-015: Network failure detection and root cause analysis in 5GC by NFV-based test environment.

## Team:YOTA-YOTA
## Team members:
- Akiyoshi shota
- Yamaguchi Yu
- Ohshima Saiga
- Tashiro Ryouga

## Challenge Theme
The objective is to detect anomalies and determine the type of anomaly using the data measured in each part of the NFV that simulates a 5G core network.

## Requirements
```
xgboost==1.5.0
scikit-learn==1.0.1
optuna==2.10.0
pandas==1.3.4
numpy==1.17.3
matplotlib==3.4.3
```

## About Dataset
The original data set can be downloaded from the following website.[Data size:73GB]
```
https://challenge.aiforgood.itu.int/match/matchitem/57
```

## Code description posted to Github
```
# Feature extraction
- dataset.py： Display the type and number of failures
- fault_location.py： Display the type of failure and the location of the failure
- relate_data_time.py：Display labels (faults) and data in chronological order
- label.py： Display of absolute path and fault type
- relate_data_time_ctm_yamaguchi.py： Display the correct label file name, fault type, and fault interface.
# data preprocessing
- key.py： Extracting feature data from a json file
- 10sec_inoctet.py： Display of values for 10 seconds and time series of data 　		　and correct answer labels 
- exlude_non_parama_data.py： Exclude files with missing data 
- make_dataset.py：Dataset creation (data extraction, preprocessing, correct answer labeling)
# Learning phase
- custom_xgboost.py： Learning with xgboost 
- test_xg_light.ipynb： Learning with light_gbm
```
