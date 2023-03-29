import mysql.connector as mysql
import os
import requests
import datetime
import time
import mysql.connector as mysql

db = mysql.connect(

    host="database-1.c8wvfa9oex9i.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd=os.environ.get('RDS_pass'),
    database='try'
)
crsr = db.cursor(buffered=True)
crsr.execute("CREATE TABLE IF NOT EXISTS BTC (DateTime timestamp , Price float(100,4 ))")
crsr.execute("CREATE TABLE IF NOT EXISTS ETH (DateTime timestamp, Price float(100, 4))")
while True:
    URL_for_BTC = f"https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    URL_for_ETH = f"https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    get_Data_BTC = requests.get(URL_for_BTC).json()
    price_BTC = str(get_Data_BTC["price"])
    current_datetime_str = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    current_datetime = datetime.datetime.strptime(current_datetime_str, "%y-%m-%d %H:%M:%S")

    get_Data_ETH = requests.get(URL_for_ETH).json()
    price_ETH = str(get_Data_ETH["price"])

    crsr.execute("INSERT INTO BTC (DateTime, Price) VALUES (%s, %s)", (current_datetime, price_BTC))
    crsr.execute("INSERT INTO ETH (DateTime, Price) VALUES (%s, %s)", (current_datetime, price_ETH))

    db.commit()
    print("Data stored")
