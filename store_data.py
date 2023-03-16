from sqlalchemy.orm import DeclarativeBase 
import requests
from sqlalchemy import String, Integer, Column
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import time
import matplotlib
# import keyboard
from datetime import timedelta
from matplotlib import pyplot as plt
# import o
# cwd = os.getcwd()
engine = create_engine("sqlite:///C:\\Users\\panka\\OneDrive\\Desktop\\KIDS\\Aryan\\Python_Projects\\CryptoStreamlit\\database.db", echo=True)

URL_for_BTC = f"https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
URL_for_ETH = f"https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

class Base(DeclarativeBase):
   pass


class BTC_prices(Base):
    __tablename__ = "BTC"

    id = Column(Integer, primary_key=True)
    price = Column(String(50))
    datetime = Column(String(50))
   


class ETH_prices(Base):
    __tablename__ = "ETH"

    id = Column(Integer, primary_key=True)
    price = Column(String(50))
    datetime = Column(String(50))
   

Base.metadata.create_all(engine)
if __name__ == "__main__":
    while True:
        get_Data_BTC = requests.get(URL_for_BTC).json()
        price_BTC = get_Data_BTC["price"]
        # print(price_BTC)
        current_datetime = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_datetime)
        get_Data_ETH = requests.get(URL_for_ETH).json()
        price_ETH = get_Data_ETH["price"]    

        with Session(engine) as session: 
            add_btc = BTC_prices(datetime=current_datetime, price=price_BTC)
            add_eth = BTC_prices(datetime=current_datetime, price=price_ETH)
            session.add(add_btc)
            session.add(add_eth)

            session.commit()
            



    