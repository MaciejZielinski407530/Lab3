import pickle
import os
import pandas as pd
import time

def save_result_to_disk(func):
    def wrapper(*args, **kwargs):

        if not os.path.exists("cached_results"):
            os.makedirs("cached_results")

        cache_file_path = f"cached_results/{args[0]}.{args[1]}"
        if os.path.exists(cache_file_path):
            if args[1] == 'pickle':
                result = pd.read_pickle(cache_file_path)
            if args[1] == 'csv':
                result = pd.read_csv(cache_file_path)
        else:
            result = func(*args, **kwargs)
            if args[1] == 'pickle':
                result.to_pickle(cache_file_path)
            if args[1] == 'csv':
                result.to_csv(cache_file_path, index=False)
        return result

    return wrapper


@save_result_to_disk
def print_10_oldest_column(a, file_type):
    url = "https://huggingface.co/datasets/imodels/credit-card/raw/main/train.csv"
    dane = pd.read_csv(url)
    oldest_10 = dane.sort_values(by='age', ascending=False).head(10)
    return oldest_10.loc[:, [a]]


start = time.time()
result1 = print_10_oldest_column('age', 'csv')
stop = time.time()
print("[csv] Pierwsze wywolanie:", stop-start)

start = time.time()
result1 = print_10_oldest_column('age', 'csv')
stop = time.time()
print("[csv] Drugie wywolanie:", stop-start)

start = time.time()
result1 = print_10_oldest_column('pay_2', 'pickle')
stop = time.time()
print("[pickle] Pierwsze wywolanie:", stop-start)

start = time.time()
result1 = print_10_oldest_column('pay_2', 'pickle')
stop = time.time()
print("[pickle] Drugie wywolanie:", stop-start)