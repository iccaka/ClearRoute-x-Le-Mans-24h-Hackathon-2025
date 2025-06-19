"""
Main module for executing the anomaly detection process on coolant temperature data.

This script reads statistical data from a CSV file and initializes an instance of the
AnomalyDetection class to calculate the anomaly score for a specific column in the dataset.
The anomaly score is computed based on the training data provided.

Key Components:
- Reads statistical data from 'data/stats.csv'.
- Initializes the AnomalyDetection class with training data from 'data/train_data.csv'.
- Calculates the anomaly score for the 'coolant_temperature' column at a specific index (144)
  in the statistics DataFrame.

Usage:
1. Ensure that the required CSV files ('data/stats.csv' and 'data/train_data.csv') are present
   in the 'data' directory.
2. Run the script to output the anomaly score for the specified coolant temperature value.

Example:
To run the script, execute:
    python main.py
"""


import pandas as pd
from anomaly_detection import AnomalyDetection

if __name__ == '__main__':
    stats_df = pd.read_csv('data/stats.csv')
    anomalyDetection = AnomalyDetection('data/train_data.csv')
    column = 'coolant_temperature'

    print(anomalyDetection.calculate_anomaly_score(column, stats_df.loc[144, column]))
