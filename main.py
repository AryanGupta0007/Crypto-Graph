
import streamlit as st
import pandas as pd
import mysql.connector as mysql
import datetime
import sys
import os
from streamlit import pyplot
from matplotlib import pyplot as plt
from streamlit import pyplot
from datetime import timedelta
try:
    db = mysql.connect(

        host="localhost",
        user="root",
        # passwd=os.environ.get('SQL_PASS'),  # password when using pycharm configurations
        # passwd=os.environ['SQL_PASS'], # password after setting password in cmd
        database="CryptoPrices")  # password when using cmd to run the script


except Exception as Error:
    print(Error)
    sys.exit()
crsr = db.cursor(buffered=True)
while True:
    st.title("Crypto Graph")
    current_datetime_str = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    current_datetime = datetime.datetime.strptime(current_datetime_str,"%y-%m-%d %H:%M:%S")
    before_1_min = current_datetime + timedelta(minutes=-1)
    # seconds = [x for x in range (1, 60)]
    result = []
    for x in range(60):
        time = before_1_min + timedelta(seconds=x)
        time = datetime.datetime.strftime(time, "%y-%m-%d %H:%M:%S")
        result.append(time)
    # result = [ for x in range (len(seconds)]
    # print(result)

    #
    # #
    #
    prices = []
    times = []
    placeholder = st.empty()
    with st.empty():
        for x in range(len(result)):
            crsr.execute("SELECT Price FROM BTC WHERE DateTime = %s", (result[x], ) )

            date = datetime.datetime.strptime(result[x], "%y-%m-%d %H:%M:%S")

            for row in crsr:
                for price in row:
                    price = float(price)
                    prices.append(price)
                    times.append(date)
            try:
                df = {"Date": times,
                "Price": prices
                }
            except:
                pass

            DF = pd.DataFrame(df)
            DF = DF.set_index("Date")
            plt.title("1 min graph")
            plt.ylabel("Prices")
            plt.xlabel("Date Time")
            plt.plot(times, prices)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            placeholder.pyplot()
