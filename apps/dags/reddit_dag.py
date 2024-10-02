from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

sys.path.insert(0, '/opt/airflow')

from pipelines.aws_s3_pipeline import aws_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 18)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='dag_reddit',
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args,
    tags=['reddit', 'etl', 'pipeline']
)

reddit = PythonOperator(
    task_id='task_reddit',
    python_callable=reddit_pipeline,
    dag=dag,
    op_kwargs={
        'file_name': f'extract_reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    }
)

s3 = PythonOperator(
    task_id='task_aws_s3',
    provide_context=True,
    python_callable=aws_s3_pipeline,
    dag=dag,
)

reddit >> s3