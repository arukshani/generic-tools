import pandas as pd
from datetime import datetime
import plotly.graph_objs as go
import plotly
import matplotlib.pyplot as plt

import plotly.express as px
from datetime import datetime

path = "/Users/rukshani/Documents/Opera/"

client_data = pd.read_csv(path+"L1_client_3s.csv" ,sep='\t',
                          names=["time", "src", "dst", "seq_number"])

rt_client_data = pd.read_csv(path+"rt_L1_client_3s.csv" ,sep='\t',
                          names=["time", "src", "dst", "seq_number"])

def get_timestamp(time_format):
    return time_format.timestamp() * 1000 * 1000

# client_data = client_data.head(200)
client_data['time_convert'] = pd.to_datetime(client_data['time'],
                        infer_datetime_format=True)
client_data['packet_time'] = pd.to_datetime(client_data.time_convert, unit='us')
client_data['timestamp']= client_data.packet_time.apply(get_timestamp)
# client_data['A_dif'] = client_data['timestamp'].diff() //diff between consecutibe rows
client_data['relative_time'] =  client_data.loc[1:, 'timestamp'] - client_data.at[0, 'timestamp']

# Retransmissions
rt_client_data['time_convert'] = pd.to_datetime(rt_client_data['time'],
                        infer_datetime_format=True)
rt_client_data['packet_time'] = pd.to_datetime(rt_client_data.time_convert, unit='us')
rt_client_data['timestamp']= rt_client_data.packet_time.apply(get_timestamp)

fig, ax = plt.subplots(figsize=(8, 6))
# ax.set_color_cycle(['red', 'black'])
plt.plot(client_data.timestamp, client_data["seq_number"], label = "Original")
plt.scatter(rt_client_data.timestamp, rt_client_data["seq_number"], marker="x", label = "Retransmissions", color='red')

# plt.scatter(client_data.relative_time, client_data["seq_number"], label = "Client")
plt.legend()
plt.xlabel('Time (us)', fontsize = 14)
plt.ylabel('Sequence Number', fontsize = 14)
plt.show()