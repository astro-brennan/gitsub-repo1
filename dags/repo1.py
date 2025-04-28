import datetime 
import importlib

from airflow.decorators import dag, task
from scripts.script1 import MyClass

@dag(start_date=datetime.datetime(2025, 1, 1), schedule='@once')
def repo1_dag():
    @task
    def printer():
        a = MyClass()
        print(a.x)

    printer()
repo1_dag()