import datetime
import logging
from airflow.decorators import dag
from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.python import PythonOperator
from shared_functions import upsert_player_data

def health_check_response(response):
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"response body: {response.text}")
    return response.status_code == 200 and response.json() == {
        "message": "API health check successful"
    }