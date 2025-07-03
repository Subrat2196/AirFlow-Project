from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments to be applied in all the tasks in the DAG
# 1. Author
default_args = {
    'owner':'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG workflow (Directed Acyclic Graph)

with DAG(
    'demo_dag_1',
    default_args=default_args,
    description="A simple dag workflow to make you understand how DAg workds in Airflow",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # Task 1: Print the current system date
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Task 2 : Sleep for 5 seconds
    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    # Set task dependencies (t1 must run before t2)
    t1 >> t2
    