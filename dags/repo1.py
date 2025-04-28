import datetime 
import importlib

from airflow.decorators import dag, task

@dag(start_date=datetime.datetime(2025, 1, 1), schedule='@once')
def repo1_dag():
    @task
    def printer():
        a = importlib.import_module("gitsub-repo1.scripts.script1.MyClass")
        print(a.x)

    printer()
repo1_dag()