from etls.reddit_etl import connect_with_reddit, extract_posts, transform_posts, load_posts_data_to_csv
from configs.envs import REDDIT_CLIENT_ID, REDDIT_SECRET_KEY, OUTPUT_PATH
import pandas as pd

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    instance = connect_with_reddit(REDDIT_CLIENT_ID, REDDIT_SECRET_KEY, 'Airflow Agent')

    posts = extract_posts(instance, subreddit, time_filter, limit)

    post_df = pd.DataFrame(posts)
    post_df = transform_posts(post_df)

    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    
    load_posts_data_to_csv(post_df, file_path)

    return file_path