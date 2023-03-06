Pandas

In the, very difficult and sometimes frustrating, search to find out about the use of Argparse and .csv files, I came upon Pandas. Pandas is a Python library used for working with data sets. It made the process of creating and manipulating .csv files and DataFrames a lot easier. Pandas is a clean way to use DataFrames, I had the feeling that there is not a lot code needede to get the outcome that is needed and it is pretty easy to learn and implement. For example, this is the way to create a .csv file out of a DataFrame:

	df = pandas.DataFrame(data)
    		with open("bought.csv", mode = "a") as file:
        	df.to_csv(file, header=file.tell()==0, index=False) 

Timedelta 

To stay with Pandas, I used Timedelta for time manipulation. This was also easy to use and to understand. By using Timestamp it is possible to set a date as ‘today’. From there you can go back or forth in time using Timedelta. This way it is possible to see the revenue, or the profit or the inventory of, for example, two days ago, or 2 weeks in the future. Here’s as small peace of code to illustrate how it’s used:

	df = pd.read_csv("sold.csv")
    		df["sell date"] = pd.to_datetime(df["sell date"])
    		if args.time > 0:
        		td = pd.Timedelta(days = int(args.time))
        		new_dt = ts + td
        		filtered_df = df[df["sell date"] <= new_dt]
        		sell_price_column = filtered_df["total price"]
        		sum_column = sell_price_column.sum()
        		print(sum_column)



Tabulate

To make nice and readable tables from the DataFrames I used Tabulate. Easy to use combined with Pandas and it gives a very clean output.
To use Tabulate you first have to read a DataFrame:

    df = pandas.read_csv("bought.csv")

Then print it using Tabulate:

    print(tabulate(df.round(decimals=2), headers="keys", showindex = False, tablefmt="outline"))


