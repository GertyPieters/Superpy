import pandas
import os
from tabulate import tabulate

DIR = "C:\\Users\\gerty\\OneDrive\\Documenten\\Winc\\hello-world\\superpy"
os.chdir(DIR)

def bought(args):
    data = {
        "id":[args.id],
        "product name":[args.product_name], 
        "count":[args.count], 
        "buy date":[args.buy_date], 
        "buy price":[args.buy_price], 
        "expiration date":[args.exp_date] 
        }
    df = pandas.DataFrame(data)
    with open("bought.csv", mode = "a") as file:
        total_price_bought = args.count * args.buy_price
        df["total price bought"] = total_price_bought
        df.round(decimals = 2)
        df.to_csv(file, header=file.tell()==0, index=False) 
    print('OK')  


def read_bought():
    df = pandas.read_csv("bought.csv")
    print(tabulate(df.round(decimals=2), headers="keys", showindex=False, tablefmt="outline"))



