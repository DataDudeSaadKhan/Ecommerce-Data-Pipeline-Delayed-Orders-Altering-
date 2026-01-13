from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# import snowflake.connector
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'email': ['datadudesaadkhan@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='order_monitoring_dag16',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='source "D:\Software Developement\Data Engineering\Ecommerce_Project\airflow_venv\Scripts\activate" && cd "D:\Software Developement\Data Engineering\Ecommerce_Project\dbt_ecommerce" && dbt run'
    )

    check_orders = BashOperator(
        task_id='check_delayed_orders',
        bash_command='source "D:\Software Developement\Data Engineering\Ecommerce_Project\airflow_venv\Scripts\activate" && python "D:\Software Developement\Data Engineering\Ecommerce_Project\airflow_project\utils\check_delayed_orders.py"'
    )

    dbt_run >> check_orders
