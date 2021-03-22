import os
import csv
import numpy as np
import pandas as pd

delimiter = ';j'
momentums = ['E', 'pt', 'eta', 'phi']
path="data\\monojet_Zp2000.0_DM_50.0_chan3.csv"
split_ratio=0.8
def normalize(df):
	df["E"] = np.log10(df["E"])
	df["pt"] = np.log10(df["pt"])
	df["eta"] = df["eta"] / 5
	df["phi"] = df["phi"] / 3
	return df

jet_arr = []
with open(path, "r") as file:
    csv = csv.reader(file)
    for event in csv:
        indices = [idx for idx,obj in enumerate(event) if delimiter in obj]
        clean_event = [float(element.split(';')[0]) for element in event]
        for i in indices:  
            jet_arr.append(clean_event[i+1: i+5])
            print(clean_event[i+1:i+5])
train_count = int(len(jet_arr) *  split_ratio)
train_df = pd.DataFrame(jet_arr[:train_count], columns=momentums)
train_df = normalize(train_df).to_pickle('data\\monojet_Zp2000.0_DM_50.0_chan3_train.pkl')

test_df = pd.DataFrame(jet_arr[train_count:], columns=momentums)
test_df = normalize(test_df).to_pickle('data\\monojet_Zp2000.0_DM_50.0_chan3_test.pkl')