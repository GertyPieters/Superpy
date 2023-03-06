import pandas as pd
import datetime as dt


def get_count_bought(id):
    df = pd.read_csv("bought.csv")
    product = df[df["id"] == id]
    if len(product) == 0:
        print("Product ID not found") 
    else:
        count_bought = product["count"].iloc[0]
        return count_bought
    #print(count_bought)

def get_count_sold(id):
    df = pd.read_csv("sold.csv")
    product = df[df["id"] == id]
    if len(product) == 0:
        print("Product ID not found") 
    else:
        count_sold = product["count"].iloc[0]
        return count_sold
    #print(count_sold)

def count_inv(id):
    count_of_bought = get_count_bought(id)
    count_of_sold = get_count_sold(id)
    count = count_of_bought - count_of_sold
    return count
