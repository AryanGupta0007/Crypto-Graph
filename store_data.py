
import mysql.connector as mysql
import os
import requests
import datetime
import time
# import keyboard
# from datetime import timedel

db = mysql.connect(

    host="localhost",
    user="root",
    # passwd=os.environ.get('SQL_PASS'), # password when using pycharm configurations
    passwd=os.environ['SQL_PASS'],
    database="CryptoPrices"
)#password when using cmd to run the script
crsr = db.cursor(buffered=True)
# #
crsr.execute("DROP TABLE IF EXISTS BTC")
crsr.execute("DROP TABLE IF EXISTS ETH")
crsr.execute("CREATE TABLE BTC (Price VARCHAR(20) ,  DateTime VARCHAR(20) )")
crsr.execute("CREATE TABLE ETH (Price VARCHAR(20) ,  DateTime VARCHAR(20) )")
while True:
    URL_for_BTC = f"https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    URL_for_ETH = f"https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    get_Data_BTC = requests.get(URL_for_BTC).json()
    price_BTC = str(get_Data_BTC["price"])
    current_datetime_str = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    current_datetime = datetime.datetime.strptime(current_datetime_str,"%y-%m-%d %H:%M:%S")

    # current_datetime = datetime
    get_Data_ETH = requests.get(URL_for_ETH).json()
    price_ETH = str(get_Data_ETH["price"])

#
    # time.sleep(1)
    # time.sleep(20)
    crsr.execute("INSERT INTO BTC (DateTime, Price) VALUES (%s, %s)", (current_datetime_str, price_BTC))
    crsr.execute("INSERT INTO ETH (DateTime, Price) VALUES (%s, %s)", (current_datetime_str, price_ETH))

    db.commit()
    print("Data stored")

        # crsr.execute()
#

    