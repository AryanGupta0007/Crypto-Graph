#importing all the required libraries
import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import time
import mysql.connector as mysql
#reading dataword when using cmd to run the script

def update_price_date():
    db = mysql.connect(

        host="database-1.c8wvfa9oex9i.us-east-1.rds.amazonaws.com",
        user="admin",
        # passwd=os.environ.get('SQL_PASS'),  # password when using pycharm configurations
        passwd="12345678",  # password after setting password in cmd
        database="try")  # password when using cmd to run the script
    crsr = db.cursor(buffered=True)
    current_datetime_str = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    current_datetime = datetime.datetime.strptime(current_datetime_str, "%y-%m-%d %H:%M:%S")
    before_1_min = current_datetime + timedelta(minutes=-1)
    crsr.execute("SELECT * FROM BTC WHERE DateTime between %s and %s ", (before_1_min, current_datetime))
    times = []
    prices = []
    for date, price in crsr:
        times.append(date)
        prices.append(price)
    df = {"Date": times,
          "Price": prices
          }
    DF = pd.DataFrame(df)
    return DF

# df['date'] = pd.to_datetime(df['date'])
#defining containers
header = st.container()
select_param = st.container()
plot_spot = st.empty()

#title
with header:
    st.title("Crypto Graph")

#function to make chart
def make_chart(df, ymin, ymax):

    fig = go.Figure(layout_yaxis_range=[ymin, ymax])
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'],           mode='lines+markers'))
    
    fig.update_layout(width=900, height=570, xaxis_title='time',
    yaxis_title='Price')
    st.write(fig)


#func call
while True:
    df = update_price_date()
    n = len(df)
    print(n)
    # print(df)
    ymax = max(df['Price'])+5
    ymin = min(df['Price'])-5
    for i in range(0, n-30, 1):
        df_tmp = df.iloc[i:i+90, :]
        with plot_spot:
            make_chart(df_tmp, ymin, ymax)
        time.sleep(0.5)
