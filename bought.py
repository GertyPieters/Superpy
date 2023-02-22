import csv
import argparse
import pandas
import datetime
import os


DIR = "C:\\Users\\gerty\\OneDrive\\Documenten\\Winc\\hello-world\\superpy"
os.chdir(DIR)

def bought(args):
    data = {
        "product name":[args.product_name], 
        "count":[args.count], 
        "buy date":[args.buy_date], 
        "buy price":[args.buy_price], 
        "expiration date":[args.exp_date] 
        }
    df = pandas.DataFrame(data)
    with open("bought.csv", mode = "a") as file:
        df.to_csv(file, header=file.tell()==0, index=False) 
    print('OK')  


def read_bought():
    df = pandas.read_csv("bought.csv")
    print(df)



"""
data = {
        "product name":[args.product_name], 
        "count":[args.count], 
        "buy date":[args.buy_date], 
        "buy price":[args.buy_price], 
        "expiration date":[args.exp_date] 
        }
    df = pandas.DataFrame(data)
    with open("bought.csv", mode = "a") as file:
        for i in df:
            if i not in df:
                new_df = pandas.DataFrame(data)
                with open("bought.csv", mode = "a") as file:
                    new_df.to_csv(file, header = file.tell()==0, index=False)
        else:  
            df.to_csv(file, header=file.tell()==0, index=False) 
            """