import datetime 
import importlib
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator 

@dag(start_date=datetime.datetime(2021, 1, 1), schedule='@daily')
def repo1_dag():
    @task
    def printer():
        a = importlib.import_module("gitsub-repo1.scripts.script1.MyClass")
        print(a.x)

repo1_dag()