from configs.envs import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import s3fs

def connect_with_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False, 
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_SECRET_ACCESS_KEY,
        )

        return s3
    except Exception as e:
        print(e)

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, bucket_object: str):
    try:
        s3.put(file_path, bucket+'/raw/'+ bucket_object)
        print('File uploaded to s3')
    except FileNotFoundError:
        print('The file was not found')