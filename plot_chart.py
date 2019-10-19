import plotly.graph_objs as go

fig = go.Figure()

rtt1 = [0.118, 0.197,0.065,0.112,0.205,0.115,0.118,0.219,0.111,0.12,0.265,0.117,0.129,0.211,0.176,0.176,0.116,0.117,
            0.097,0.097,0.058,0.058,0.057,0.059,0.158,0.16,0.059,0.059,0.026,0.072,0.059,0.06]

hosts = ["h" +  str(i) for i in range(1,33)]

rtt2 = [0.276,0.197,0.165,0.112,0.205,0.115,0.118,0.219,0.111,0.12,0.265,0.117,0.129,0.211,0.176,0.176,0.116,0.117,0.097,
0.116,0.058,0.059,0.057,0.059,0.158,0.16,0.059,0.059,0.026,0.072,0.059,0.06]


fig.add_trace(go.Scatter(x=hosts, y= rtt1, name='Single Table'))
fig.add_trace(go.Scatter(x=hosts, y= rtt2, name='Multiple table'))

# Edit the layout
fig.update_layout(xaxis_title='Number of hosts', yaxis_title='RTT')


fig.show()