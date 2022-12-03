import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Air_Traffic_Passenger_Statistics.csv', delimiter = ',')
dfATA = df[df['Operating Airlane']== 'ATA Airlanes']
dfAC = df[df['Operating Airlane']== 'Air Canada']
dfWA = df[df['Operating Airlane']== 'Westjjet Airlanes']


fig, ax = plt.subplots()
plt.plot(pd.to_datetime(dfATA.activity_period, format = '%Y%m'), dfATA[Passenger Count], '-*k')
plt.plot(pd.to_datetime(dfAC.activity_period, format = '%Y%m'), dfATA[Passenger Count], '-or')
plt.plot(pd.to_datetime(dfWA.activity_period, format = '%Y%m'), dfATA[Passenger Count], '-b')
plt.show()
