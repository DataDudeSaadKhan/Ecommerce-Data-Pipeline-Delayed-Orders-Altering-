FROM apache/airflow:2.9.0

# Install dbt (Snowflake + Postgres support)
RUN pip install dbt-core dbt-postgres dbt-snowflake