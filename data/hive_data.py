import yaml
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import random
from io import BytesIO
import boto3
from minio import Minio
import os
import math

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

datalake_config = config['datalake']

endpoint = datalake_config['endpoint']
bucket_name = datalake_config['bucket_name']
access_key = datalake_config['access_key']
secret_key = datalake_config['secret_key']

minio_client = Minio(
    endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False
)

student_ids = ['student001', 'student002', 'student003']
subject_ids = ['subject001', 'subject002', 'subject003', 'subject004', 'subject005', 'subject006']

data = []
id_counter = 1

for student_id in student_ids:
    for subject_id in subject_ids:
        score_id = f'score{str(id_counter).zfill(3)}'
        score = round(random.uniform(5, 10) * 2) / 2
        data.append({'id': score_id, 'student_id': student_id, 'subject_id': subject_id, 'score': score})
        id_counter += 1

df = pd.DataFrame(data)

records_per_file = 5
num_files = (len(df) // records_per_file) + (1 if len(df) % records_per_file != 0 else 0)

for i in range(num_files):
    start_idx = i * records_per_file
    end_idx = min((i + 1) * records_per_file, len(df))
    df_chunk = df.iloc[start_idx:end_idx]

    table = pa.Table.from_pandas(df_chunk)

    parquet_buffer = BytesIO()
    pq.write_table(table, parquet_buffer)
    parquet_buffer.seek(0)

    file_name = f'score_{i + 1}.parquet'

    minio_client.put_object(
        bucket_name,
        f'data/{file_name}',
        parquet_buffer,
        parquet_buffer.getbuffer().nbytes
    )

    print(f"File {file_name} has been successfully uploaded to MinIO at 'trino/data/{file_name}'")
