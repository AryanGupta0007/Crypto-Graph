import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import datetime
from datetime import timedelta
from sqlalchemy.orm import sessionmaker
from store_data import ETH_prices
from store_data import BTC_prices
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy.orm import Session
from streamlit import pyplot
from matplotlib import pyplot as plt
import time
# database_url = "C:\\Users\\panka\\OneDrive\\Desktop\\KIDS\\Aryan\\Python_Projects\\CryptoStreamlit\\database.db"
engine = create_engine("sqlite:///C:\\Users\\panka\\OneDrive\\Desktop\\KIDS\\Aryan\\Python_Projects\\CryptoStreamlit\\database.db")
while True:
    st.title("Crypto Graph")

    current_datetime = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        
    current_time1 = datetime.datetime.strptime(current_datetime, "%H:%M:%S %d-%m-%Y")
    # print(f"current time {current_time1}")
    time1 = current_time1 - timedelta(minutes=1)
    # print(f"1min before {time1}")
    # time.sleep(10)    

    result = []
    current_time_object = current_time1
    time1_object = time1
    initial_time_string = datetime.datetime.strftime(time1_object, "%H:%M:%S %d-%m-%Y")
    result.append(initial_time_string)

    while current_time_object >= time1_object:
        time1_object += datetime.timedelta(seconds=1)
        time1_str = datetime.datetime.strftime(time1_object, "%H:%M:%S %d-%m-%Y")
        result.append(time1_str)
    # print(result)
    # time.sleep(20)
    times = []
    prices = []
    placeholder = st.empty()
    with st.empty():
        for x in range(len(result)):
            with Session(engine) as session:
                data = session.query(BTC_prices).filter(BTC_prices.datetime==result[x]).first()
                # print(data)
                # time.sleep(5)

                if  data:
                    date = datetime.datetime.strptime(data.datetime, "%H:%M:%S %d-%m-%Y")
                    price = float(data.price)
                    times.append(date)  
                    prices.append(price)
                    df = {"Date": times, 
                    "Price": prices
                    }
                    DF = pd.DataFrame(df)
                    DF = DF.set_index("Date")
                    plt.title("1 min graph")
                    plt.ylabel("Prices")
                    plt.xlabel("Date Time")
                    plt.plot(times, prices)
                    st.set_option('deprecation.showPyplotGlobalUse', False)
                    placeholder.pyplot() 

                    # placeholder.line_chart(DF)
                    # pyplot(fig)
                    # plt.title("1 min graph")
                    # plt.ylabel("Prices")
                    # plt.xlabel("Date Time")
                    # plt.plot(times, prices)        
            # # print(dictionary)
            # # time.sleep(10)

    