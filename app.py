"""
Anomaly Detection API

This module implements a FastAPI application that provides an API endpoint to retrieve statistical data
and their corresponding anomaly scores. The application reads statistical data from a CSV file and uses
an anomaly detection algorithm to calculate the anomaly score for each statistic at a given time step.

Dependencies:
- pandas: For data manipulation and reading CSV files.
- fastapi: For creating the web API.
- starlette.responses: For returning JSON responses.
- anomaly_detection: Custom module for anomaly detection logic.
- color_getter: Custom module for color interpolation based on anomaly scores.

Constants:
- DEFAULT_LOWER_BOUND_COLOR (str): The default color for the lower bound of the anomaly score.
- DEFAULT_UPPER_BOUND_COLOR (str): The default color for the upper bound of the anomaly score.

Global Variables:
- stats_df (DataFrame): A pandas DataFrame containing statistical data loaded from 'stats.csv'.
- anomalyDetection (AnomalyDetection): An instance of the AnomalyDetection class initialized with 'train_data.csv'.

API Endpoints:
- GET /api/stats/{time_step}:
    Retrieves the anomaly scores for all statistics at the specified time step.

    Parameters:
    - time_step (int): The index of the time step for which to retrieve the statistics.

    Returns:
    - JSONResponse: A JSON object containing the anomaly scores and corresponding colors for each statistic.
      The structure of the response is as follows:
      {
          "result": {
              "statistic_name": {
                  "value": anomaly_score,
                  "color": interpolated_color
              },
              ...
          }
      }
"""

import pandas as pd
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from anomaly_detection import AnomalyDetection
from color_getter import interpolate_color

app = FastAPI()

DEFAULT_LOWER_BOUND_COLOR = '#000000'
DEFAULT_UPPER_BOUND_COLOR = '#FFFFFF'
stats_df = pd.read_csv('data/stats.csv')
anomalyDetection = AnomalyDetection('data/train_data.csv')


@app.get('/api/stats/{time_step}')
def get_stats(time_step: int) -> JSONResponse:
    """
    Retrieve the anomaly scores for all statistics at the specified time step.

    Parameters:
    - time_step (int): The index of the time step for which to retrieve the statistics.

    Returns:
    - JSONResponse: A JSON object containing the anomaly scores and corresponding colors for each statistic.
    """

    columns = stats_df.columns
    results = {}

    for x in columns:
        result = anomalyDetection.calculate_anomaly_score(x, stats_df.loc[time_step, x])
        anomaly_detection_result = {
            'value': result,
            'color': interpolate_color(DEFAULT_LOWER_BOUND_COLOR, DEFAULT_UPPER_BOUND_COLOR, result)
        }
        results[x] = anomaly_detection_result

    return JSONResponse(content={'result': results})
