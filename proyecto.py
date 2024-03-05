from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG

def print_hello():
    print('¡Ejecucion del DAG proyecto!')

dag = DAG('proyecto1', description='DAG del proyecto1',
            schedule_interval='@daily',
            start_date=datetime(2024, 3, 4),
            catchup=False)

proyecto1_operator = PythonOperator(task_id='proyecto_1', python_callable=print_hello, dag=dag)

email_operator = EmailOperator(
            task_id='send_email',
            to="kevinpruebaagetic2024@gmail.com",  
            subject="Correo de de aviso de ejecucion",  
            html_content=None,  
            dag=dag
        )
            
proyecto1_operator >> email_operator
