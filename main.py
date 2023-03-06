# Imports
import argparse
import os
import pandas as pd
from tabulate import tabulate
from datetime import datetime
from bought import bought, read_bought
from sold import sold
from functions_super import count_inv, get_count_bought

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

parser = argparse.ArgumentParser(description = "Stock overview")
subparser = parser.add_subparsers(dest = "command")

ts = pd.Timestamp("2022-12-12") # The day it is "today", from this day the time wil go a day (or days) forward or back.

buy = subparser.add_parser("buy") # Adding products to the bought.csv file, these are the product that are in stock.
buy.add_argument("id", type = int, help = "Fill in the ID of the bought product.")
buy.add_argument("product_name", type = str, help = "Fill in the product name of the bought product.")
buy.add_argument("count", type = int, help = "Fill in the number of product bought.")
buy.add_argument("buy_date", type = str, help = "Fill in the buy date of the product (yyyy-mm-dd).")
buy.add_argument("buy_price", type = float, help = "Fill in the payd price for the bought product.")
buy.add_argument("exp_date", type = str, help = "Fill in the expiration date of the product (yyyy-mm-dd).")

read = subparser.add_parser("read") # Type this in to see what products are in the bought.csv file.

price = subparser.add_parser("price")
price.add_argument("id", type = int, help = "Fill in the ID of the product to see the price the product is bought for.")

count = subparser.add_parser("count")
count.add_argument("id", type = int, help = "Fill in the ID of the product to see the amount of the product that is bought.")

write = subparser.add_parser("write") # This writes the products that are sold to the inventory.csv file.
write.add_argument("id", type = int, help = "Fill in the ID of the sold product to get the sold product to the inventory list.")

sell = subparser.add_parser("sold") # This writes the sold product to the sold.csv file.
sell.add_argument("id", type = int, help = "Fill in the ID of the sold product")
sell.add_argument("count", type = int, help = "Fill in the number of product that are sold")
sell.add_argument("sell_date", type = str, help = "Fill in the selling date of the sold product (yyyy-mm-dd).")
sell.add_argument("sell_price", type = float, help = "Fill in the payd price for the sold product.")

inventory = subparser.add_parser("inventory") # This writes the products from the bought file inventory file and if a product is sold, by filling in the ID of that product, the info will change in the inventory file.
inventory.add_argument("time", type = int, default = 0, help = "Advance the time or go back in time.\n For example: fill in 'time 1' to go one day into the future\n and 'time -2' to go two days back in time\n Fill in 'time 0' to see the inventory of today")

revenue = subparser.add_parser("revenue") # This shows the revenue of the given day.
revenue.add_argument("time", type = int, default=0, help = "Fill in the number of days you want to look ahead (for example: 2) or back (for example: -1). For the revenue of today fill in 0.")

revenuemonth = subparser.add_parser("revenuemonth") # This shows the revenue of the given month in the given year.
revenuemonth.add_argument("month", type = int, help = "Fill in the month you want to see the the revenue of. Januari = 1, Februari = 2, March = 3, etc.")
revenuemonth.add_argument("year", type = int, help = "Fill in the year of the month you want to see the revenue of like 'yyyy'")

revenueyear = subparser.add_parser("revenueyear") # This shows the revenue of the given year.
revenueyear.add_argument("year", type = int, help = "Fill in the year you want to see the revenue of like 'yyyy'")

profit = subparser.add_parser("profit") # This shows the profit of the given day.
profit.add_argument("time", type = int, default=0, help = "Fill in the number of days you want to look ahead (for example: 2) or back (for example: -1) to see the profit of that day. For the profit of today fill in 0.")

profitmonth = subparser.add_parser("profitmonth") # This shows the profit of the given month and the given year.
profitmonth.add_argument("month", type=int, help="Fill in the month you want to see the the profit of. Januari = 1, Februari = 2, March = 3, etc.")
profitmonth.add_argument("year", type=int, help="Fill in the year of the month you want to see the profit of like 'yyyy'")

profityear = subparser.add_parser("profityear") # This shows the profit of the given year.
profityear.add_argument("year", type=int, help="Fill in the year you want to see the revenue of like 'yyyy'")

args = parser.parse_args()

# Shows the price belonging to the product by filling in its ID.
def get_buy_price():
    df = pd.read_csv("bought.csv")
    product = df[df["id"] == args.id]
    if len(product) == 0:
        print("Product ID is not found, first enter the product into the bought.csv file.") 
    else:
        price = product.iloc[0]["buy price"]
        print(price)

# Writes the bought products to the inventory and changes the product to be sold by filling in the ID of the sold product.
def inv():
    if os.path.isfile("inventory.csv"):
        df_inv = pd.read_csv("inventory.csv")
        df2 = pd.read_csv("sold.csv")
        if args.id not in df2["id"].values:
            print("Product had not been sold yet, or the product ID is not known (yet).")
            return
        sell_date = df2.loc[df2["id"] == args.id, "sell date"].values[0]
        df_inv.loc[df_inv["id"] == args.id, "count"] = count_inv(args.id)
        df_inv.loc[df_inv["id"] == args.id, "sell date"] = sell_date
        df_inv.to_csv("inventory.csv", index = False)   
        print(tabulate(df_inv, headers="keys", showindex=False, tablefmt="outline"))
    else:
        with open("inventory.csv", "a+") as new_file:
            df = pd.read_csv("bought.csv")
            df1 = pd.read_csv("sold.csv")
            if args.id not in df1["id"].values:
                print("Product had not been sold yet, or the product ID is not known (yet).")
                return
            sell_date = df1.loc[df1["id"] == args.id, "sell date"].values[0]
            df.loc[df["id"] == args.id, "count"] = count_inv(args.id)
            df["sell date"] = sell_date
            df.loc[df["id"] != args.id, "sell date"] = float('nan')        
            df.to_csv(new_file, index=False)
            print(tabulate(df, headers="keys", showindex=False, tablefmt="outline"))

# Shows the inventory of the given day, so you can look back, look at today or in the future.
def advanced_time():
    df = pd.read_csv("inventory.csv")
    df["buy date"] = pd.to_datetime(df["buy date"])
    df["sell date"] = pd.to_datetime(df["sell date"])
    df["expiration date"] = pd.to_datetime(df["expiration date"])
    df["sell date"].fillna(df["buy date"], inplace = True)    
    if args.time > 0:
        td = pd.Timedelta(days = int(args.time))
        new_dt = ts + td
        df.drop(df[df["expiration date"] <= new_dt].index, inplace = True)
        filtered_df = df[(df["sell date"] <= new_dt) & (df["buy date"] <= new_dt)]
        print(tabulate(filtered_df, headers="keys", showindex=False, tablefmt="outline"))
        return filtered_df
    elif args.time < 0:
        td = pd.Timedelta(days = int(-args.time))
        new_dt = ts - td
        df.drop(df[df["expiration date"] <= new_dt].index, inplace = True)
        filtered_df = df[(df["sell date"] <= new_dt) & (df["buy date"] <= new_dt)]
        print(tabulate(filtered_df, headers="keys", showindex=False, tablefmt="outline"))
        return filtered_df
    elif args.time == 0:
        df.drop(df[df["expiration date"] <= ts].index, inplace = True)
        filtered_df = df[(df["sell date"] <= ts) & (df["buy date"] <= ts)]
        print(tabulate(filtered_df, headers="keys", showindex=False, tablefmt="outline"))
        return filtered_df

# Gives the revenue of the given day, so you can look back, look at today or in the future. 
def rev():
    df = pd.read_csv("sold.csv")
    df["sell date"] = pd.to_datetime(df["sell date"])
    if args.time > 0:
        td = pd.Timedelta(days = int(args.time))
        new_dt = ts + td
        filtered_df = df[df["sell date"] <= new_dt]
        sell_price_column = filtered_df["total price"]
        sum_column = sell_price_column.sum()
        print(sum_column)
    elif args.time < 0:
        td = pd.Timedelta(days = int(-args.time))
        new_dt = ts - td
        filtered_df = df[df["sell date"] <= new_dt]
        sell_price_column = filtered_df["total price"]
        sum_column = sell_price_column.sum()
        print(sum_column)       
    elif args.time == 0:
        filtered_df = df[df["sell date"] <= ts]
        sell_price_column = filtered_df["total price"]
        sum_column = sell_price_column.sum()
        print(sum_column)    

# Gives the revenue of the given month of the given year.
def rev_month():
    df = pd.read_csv("inventory.csv")
    df["buy date"] = pd.to_datetime(df["buy date"])
    df["sell date"] = pd.to_datetime(df["sell date"])
    revenue_month = df[((df["buy date"].dt.month == args.month) & (df["buy date"].dt.year == args.year)) | ((df["sell date"].dt.month == args.month) & (df["sell date"].dt.year == args.year))]
    total_revenue_month = revenue_month["total price bought"].sum()
    print(total_revenue_month.round(2))

# Gives the revenue of the given year.
def rev_year():
    df = pd.read_csv("inventory.csv")
    df["buy date"] = pd.to_datetime(df["buy date"])
    df["sell date"] = pd.to_datetime(df["sell date"])
    revenue_year = df[((df["buy date"].dt.year == args.year) | (df["sell date"].dt.year == args.year))]
    total_revenue_year = revenue_year["total price bought"].sum()
    print(total_revenue_year.round(2))

# Gives the profit of the given day, so you can look back, look at today or in the future. 
def prof(): 
    sell_df = pd.read_csv("sold.csv")
    sell_df["sell date"] = pd.to_datetime(sell_df["sell date"])
    bought_df = pd.read_csv("inventory.csv")
    bought_df["sell date"] = pd.to_datetime(bought_df["sell date"])
    if args.time > 0:
        td = pd.Timedelta(days = int(args.time))
        new_dt = ts + td
        df1 = sell_df[sell_df["sell date"] <= new_dt]
        sell_price_column = df1["total price"]
        sum_sold = sell_price_column.sum()
        df2 = bought_df[bought_df["sell date"] <= new_dt]
        total_price_column = df2["total price bought"]
        sum_bought = total_price_column.sum()
        profit = sum_bought - sum_sold
        print(profit.round(2))
    elif args.time < 0:
        td = pd.Timedelta(days = int(-args.time))
        new_dt = ts - td
        df1 = sell_df[sell_df["sell date"] <= new_dt]
        sell_price_column = df1["total price"]
        sum_sold = sell_price_column.sum()
        df2 = bought_df[bought_df["sell date"] <= new_dt]
        total_price_column = df2["total price bought"]
        sum_bought = total_price_column.sum()
        profit = sum_bought - sum_sold
        print(profit.round(2))   
    elif args.time == 0:
        df1 = sell_df[sell_df["sell date"] <= ts]
        sell_price_column = df1["total price"]
        sum_sold = sell_price_column.sum() 
        df2 = bought_df[bought_df["sell date"] <= ts]
        total_price_column = df2["total price bought"]
        sum_bought = total_price_column.sum()
        profit = sum_bought - sum_sold
        print(profit.round(2))   

# Gives the profit of the given month of the given year.
def prof_month():
    buy_df = pd.read_csv("inventory.csv")
    buy_df["buy date"] = pd.to_datetime(buy_df["buy date"])
    sell_df = pd.read_csv("sold.csv")
    sell_df["sell date"] = pd.to_datetime(sell_df["sell date"])
    profit = buy_df[((buy_df["buy date"].dt.month == args.month) & (buy_df["buy date"].dt.year == args.year)) | ((sell_df["sell date"].dt.month == args.month) & (sell_df["sell date"].dt.year == args.year))]
    total_price_column = profit["total price bought"].sum()
    sell_price_column = sell_df["total price"]
    sum_sold = sell_price_column.sum()
    sum_bought = total_price_column.sum()
    profit_month = sum_bought - sum_sold
    print(profit_month.round(2))

# Gives the profit of the given year.
def prof_year():
    buy_df = pd.read_csv("inventory.csv")
    buy_df["buy date"] = pd.to_datetime(buy_df["buy date"])
    sell_df = pd.read_csv("sold.csv")
    sell_df["sell date"] = pd.to_datetime(sell_df["sell date"])
    profit = buy_df[((buy_df["buy date"].dt.year == args.year) | (sell_df["sell date"].dt.year == args.year))]
    total_price_column = profit["total price bought"].sum()
    sell_price_column = sell_df["total price"]
    sum_sold = sell_price_column.sum()
    sum_bought = total_price_column.sum()
    profit_year = sum_bought - sum_sold
    print(profit_year.round(2))

if args.command == "buy":
    bought(args)
if args.command == "read":
    read_bought()
if args.command == "sold":
    sold(args)
if args.command == "revenue":
    rev()
if args.command == "revenuemonth":
    rev_month()
if args.command == "revenueyear":
    rev_year()
if args.command == "profit":
    prof()
if args.command == "profitmonth":
    prof_month()
if args.command == "profityear":
    prof_year()
if args.command == "price":
    get_buy_price()
if args.command == "count":
    get_count_bought()
if args.command == "write":
    inv()
if args.command == "inventory":
    advanced_time()
