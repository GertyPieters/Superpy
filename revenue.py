import pandas as pd

def rev():
    df = pd.read_csv("sold.csv")
    sell_price_column = df["sell price"] 
    sum_column = sell_price_column.sum()
    print(sum_column)


    