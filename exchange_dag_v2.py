from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.operators.http import SimpleHttpOperator


with DAG(
    dag_id='test',
    default_args={
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        },
    description='simply ETL for practicum',
    schedule_interval=timedelta(hours=3),
    start_date=datetime(2022, 3, 16),
    catchup=False,
    is_paused_upon_creation= False,
    tags=['test']
) as dag:

    def get_today_date():
        from datetime import datetime
        today = datetime.today().strftime('%Y-%m-%d')
        return today
    
    # Task 1: get data from https://api.exchangerate.host
    get_data = SimpleHttpOperator(
         task_id="get_data",
         http_conn_id="TEST_HTTP",
         endpoint="/timeseries", 
         method="GET",
         data={'start_date': get_today_date(), 'end_date': get_today_date(), 'base': 'BTC', 'symbols': 'USD'},
         response_filter=lambda response: response.json()['rates'][get_today_date()]['USD']
    )
    
    # Task 2: insert to destination table t_pairs_value_hist
    insert_to_dest = PostgresOperator(
        
        task_id="insert_to_dest",
        postgres_conn_id="TEST_PG",
        sql="./insert_to_t_pairs_value_hist_v2.sql",
        parameters={'pair_name': 'BTC/USD', 
                    'calendar_dt': get_today_date()
                }
    )

    get_data >> insert_to_dest
