import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame
from pyspark.sql.functions import concat_ws

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

AmazonS3_source = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, 
    connection_type="s3", 
    format="csv", 
    connection_options={"paths": ["s3://s3-reddit-88qiu9/raw/"], "recurse": True}, 
    transformation_ctx="AmazonS3_source"
)

# Convert DynamicFrame to DataFrame
df = AmazonS3_source.toDF()

# Concatenate the three columns into a single column
df_combined = df.withColumn('ESS_updated', concat_ws('-', df['edited'], df['spoiler'], df['stickied']))
df_combined = df_combined.drop('edited', 'spoiler', 'stickied')

# Convert back to DynamicFrame
S3bucket_node_combined = DynamicFrame.fromDF(df_combined, glueContext, 'S3bucket_node_combined')

AmazonS3_target = glueContext.write_dynamic_frame.from_options(
    frame=S3bucket_node_combined, 
    connection_type="s3", 
    format="csv", 
    connection_options={"path": "s3://s3-reddit-88qiu9/trans/", "partitionKeys": []}, 
    transformation_ctx="AmazonS3_target"
)

job.commit()