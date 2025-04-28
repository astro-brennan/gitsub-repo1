import datetime 

from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator 

from scripts.script1 import MyClass

@dag(start_date=datetime.datetime(2021, 1, 1), schedule='@daily')
def repo1_dag():
    @task
    def printer():
        a = MyClass()
        print(MyClass.x)

repo1_dag()