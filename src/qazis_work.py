import pandas as pd


def load_data(): 
    contracts_df = pd.read_csv('../data/contracts.csv')
    customers_df = pd.read_csv('../data/customers.csv')
    return contracts_df, customers_df


def join_data(contracts_df, customers_df):
    return pd.merge(contracts_df, customers_df, left_on='customer_id', right_on='id')
   

def convert_str_float(join_df):
    join_df['deposit'] = join_df['deposit'].str.replace('$', '')
    join_df['deposit'] = join_df['deposit'].str.replace(',', '').astype(float)

    join_df['monthly_amt'] = join_df['monthly_amt'].str.replace('$', '')
    join_df['monthly_amt'] = join_df['monthly_amt'].str.replace(',', '').astype(float)

    return join_df


def add_sale_column(join_df):
    join_df['sale'] = pd.Series(join_df['deposit']+
        join_df['monthly_amt']*join_df['contract_term'])
      
    return join_df


def group_data_by_state(join_df):
    return join_df.groupby('state').agg({'sale': 'sum'})
    
   
    