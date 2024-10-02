FROM apache/airflow:latest-python3.12

COPY requirements.txt /opt/airflow/

USER root

RUN apt-get update && \
    apt-get install -y gcc python3-dev curl

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
