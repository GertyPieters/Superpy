import pandas as pd

def prof():
    sell_df = pd.read_csv("sold.csv")
    buy_df = pd.read_csv("bought.csv")

    sold_count = sell_df["sell price"]
    sum_sold = sold_count.sum()

    bought_count = buy_df["buy price"]
    sum_bought = bought_count.sum()

    profit = sum_bought - sum_sold
    print(profit)
    
    