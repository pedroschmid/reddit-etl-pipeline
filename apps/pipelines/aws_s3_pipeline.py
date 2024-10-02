from etls.aws_s3_etl import connect_with_s3, upload_to_s3
from configs.envs import AWS_BUCKET_NAME

def aws_s3_pipeline(**kwargs):
    file_path = kwargs['ti'].xcom_pull(task_ids='task_reddit', key='return_value')

    s3 = connect_with_s3()

    file_name = file_path.split('/')[-1]
    
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_name)