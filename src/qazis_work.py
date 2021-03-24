import pandas as pd

def load_data(): 
    contracts_df = pd.read_csv('../data/contracts.csv')
    customers_df = pd.read_csv('../data/customers.csv')
    return contracts_df, customers_df