# -*- coding: utf-8 -*-
"""Complete data pipeline python code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YNDDy3a3FNMND-UJycP2kK7gDIXuwuz-

**Project - Data pipelines with Redis**

In this project, we have managed to create and design a data pipeline that extracts data from a CSV file, caches it in Redis for faster retrieval, transforms the data to clean, structure, and format it, and finally loads the transformed data into a Postgres database. I have managed to well-organized the code to make it easy to understand, with clear comments explaining each step of the process.

The Python code provided defines a data pipeline that extracts data from a CSV file, caches the data in Redis for faster retrieval, transforms the data, and loads it into a Postgres database.

The extract_data() function uses pandas to extract the data from the CSV file and caches it in Redis using a Redis client object. The transform_data() function retrieves the data from Redis, cleans, structures and formats it into a new data frame, and returns the transformed data. Finally, the load_data() function connects to the Postgres database, creates a table, and inserts the transformed data into the database.

The data_pipeline() function is the main function that orchestrates the data pipeline by calling extract_data(), transform_data(), and load_data() in sequence.

This data pipeline can be useful for handling large amounts of data efficiently and reliably by leveraging Redis caching and Postgres for persistent storage.
"""

!pip install redis

#Importing the required libraries
import pandas as pd
import psycopg2
import redis

# Redis Cloud Instance Information
redis_host = 'redis-15321.c114.us-east-1-4.ec2.cloud.redislabs.com'
redis_port = 15321
redis_password = 'kNCwxO32b7hdUiTqekLaZlH3TxkaMFY3'

# Postgres Database Information
pg_host = '35.237.226.12'
pg_database = 'telecommunications_data'
pg_port = 5432
pg_user = 'postgres'
pg_password = 'password'

# Redis Client Object
redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

# Redis Client Object
redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

def extract_data():
    """
    Extract data from CSV file and cache in Redis for faster retrieval
    """
    try:
        # Extract data from CSV file using pandas
        data = pd.read_csv('customer_call_logs.csv')

        # Cache data in Redis for faster retrieval
        redis_client.set('customer_call_logs', data.to_json())

        print('Data extraction successful.')
    
    except Exception as e:
        print('An error occurred while extracting data:', e)


#Let us define the transfrom_data() fucntion
def transform_data():
    """
    Retrieve data from Redis cache and transform (clean, structure, format)
    """
    try:
        # Retrieve data from Redis cache
        data = pd.read_json(redis_client.get('customer_call_logs').decode('utf-8'))

        # Transform data (clean, structure, format)
        data['call_cost_usd'] = data['call_cost'].apply(lambda x: float(x[1:]))
        data['call_date'] = pd.to_datetime(data['call_date'])
        data['call_duration_min'] = data['call_duration'].apply(lambda x: float(x.split(':')[0]) + float(x.split(':')[1])/60)
        transformed_data = data[['customer_id', 'call_cost_usd', 'call_destination', 'call_date', 'call_duration_min']]

        print('Data transformation successful.')
        return transformed_data
    
    except Exception as e:
        print('An error occurred while transforming data:', e)

#Let us define the load_data() fucntion
def load_data(transformed_data):
    """
    Connect to Postgres database and load transformed data
    """
    try:
        # Connect to Postgres database
        conn = psycopg2.connect(host=pg_host, database=pg_database, user=pg_user, password=pg_password)

        # Create a cursor object
        cur = conn.cursor()

        # Create a table to store the data
        cur.execute('CREATE TABLE IF NOT EXISTS customer_call_logs (\
                     customer_id INT,\
                     call_cost_usd FLOAT,\
                     call_destination VARCHAR,\
                     call_date TIMESTAMP,\
                     call_duration_min FLOAT\
                     )')

        # Insert the transformed data into the database
        for i, row in transformed_data.iterrows():
            cur.execute(f"INSERT INTO customer_call_logs (customer_id, call_cost_usd, call_destination, call_date, call_duration_min) VALUES ({row['customer_id']}, {row['call_cost_usd']}, '{row['call_destination']}', '{row['call_date']}', {row['call_duration_min']})")

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        print('Data loading successful.')
    
    except Exception as e:
        print('An error occurred while loading data:', e)


#Defining the main function

def data_pipeline():
    """
    Data pipeline function that extracts, transforms, and loads data
    """
    extract_data()
    transformed_data = transform_data()
    load_data(transformed_data)

if __name__ == '__main__':
    # Run the data pipeline function
    data_pipeline()