# Week 8 Data Pipelines with Redis, Python and PostgreSQL database
Week 8 Data Pipelines with Redis, Python and PostgreSQL database

This project involves building a data pipeline to extract, transform, and load customer call logs data from a CSV file to a PostgreSQL database. The pipeline processes customer call logs from a CSV file, transforms them, and loads them into a PostgreSQL database. The pipeline is built using Python and utilizes Pandas for data extraction and transformation, Redis for caching, and psycopg2 for database connection and data loading. The data pipeline is designed to ensure efficient data processing and is implemented with best practices such as logging, error handling, and data validation. The pipeline is documented to highlight these best practices and to provide recommendations for deployment and running the pipeline with a cloud-based provider.

The data pipeline consists of three main functions:

* Extract Data: This function reads the customer call logs from a CSV file using pandas and caches them in Redis for faster retrieval.
* Transform Data: This function retrieves the customer call logs from Redis, performs data cleaning and structuring, and formats the data for loading into the PostgreSQL database.
* Load Data: This function connects to the PostgreSQL database, creates a table for storing the customer call logs if it doesn't exist, and loads the transformed data into the database.

The pipeline is designed to be modular and scalable, making it easy to add or remove steps as needed. It also follows best practices for data processing, including data validation, error handling, and secure database connectivity.

# Best Practices
Some of the best practices used in this project include:

* Modularity: The data pipeline is designed to be modular, with each function performing a specific task. This makes it easy to update or replace individual steps without affecting the rest of the pipeline.
* Testing: The project includes unit tests for each function in the data pipeline, ensuring that the code is working as expected and can catch errors early on.
* Security: The project uses secure database connectivity with psycopg2, which encrypts passwords and prevents SQL injection attacks.

# Deployment and Running the Pipeline
To deploy and run the pipeline on a cloud-based provider, the following steps can be taken:
* Clone the project repository from GitHub or GitLab.
* Set up a PostgreSQL database instance on the cloud provider and note down the host, database, username, and password information.
* Set up a Redis Cloud instance on the cloud provider and note down the host, port, and password information.
* Update the pg_host, pg_database, pg_user, pg_password, redis_host, redis_port, and redis_password variables in the data_pipeline.py file with the appropriate information.
* Run the data_pipeline.py file using a Python interpreter to extract, transform, and load the data into the PostgreSQL database.

# Conclusion
This data pipeline provides a scalable and modular solution for processing customer call logs and storing them in a PostgreSQL database. By following best practices for data processing and secure database connectivity, it ensures the reliability and security of the data.

For the purpose of this assignment, I have included a link to a Google Cloud Colab notebook which has modulzarized, well documented and commented data pipeline code for this project.
In the Assignmentfile folder, I have included the Documentation of the pipeline as both .py and .pynb files, the ReadMe file and Complete data pipeline for your perusal.

Google colab link:  https://colab.research.google.com/drive/1P2JCET-9byKwE1VPyQIoXeaQf0rCssQT?usp=sharing
