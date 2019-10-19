import plotly.graph_objs as go

rtt_single = [0.118, 0.197, 0.065, 0.112, 0.205, 0.115, 0.118, 0.219, 0.111, 0.12, 0.265, 0.117, 0.129, 0.211, 0.176,
              0.176, 0.116, 0.117,
              0.097, 0.097, 0.058, 0.058, 0.057, 0.059, 0.158, 0.16, 0.059, 0.059, 0.026, 0.072, 0.059, 0.06]

rtt_multiple = [0.276, 0.197, 0.165, 0.112, 0.205, 0.115, 0.118, 0.219, 0.111, 0.12, 0.265, 0.117, 0.129, 0.211, 0.176,
                0.176, 0.116, 0.117, 0.097,
                0.116, 0.058, 0.059, 0.057, 0.059, 0.158, 0.16, 0.059, 0.059, 0.026, 0.072, 0.059, 0.06]

jitter_single = [0.12, 0.44, 0.54, 0.56, 0.55, 0.12, 0.32, 0.09, 0.02, 0.04, 0.09, 0.029, 0.12, 0.099, 0.099, 0.11,
                 0.07, 0.05, 0.04, 0.01, 0.14, 0.08, 0.01, 0.09, 0.11, 0.01, 0.08, 0.11, 0.09, 0.08, 0.1, 0.04]

jitter_multiple = [0.12, 0.44, 0.54, 0.56, 0.55, 0.12, 0.32, 0.09, 0.02, 0.04, 0.09, 0.029, 0.12, 0.099, 0.099, 0.11,
                   0.07, 0.05, 0.04, 0.01,
                   0.14, 0.08, 0.01, 0.09, 0.11, 0.01, 0.08, 0.11, 0.09, 0.08, 0.1, 0.04]

packet_loss_single = [16, 11, 2, 0, 4, 4, 2, 8, 2, 4, 2, 4, 5, 8, 8, 1, 0, 2, 5, 4, 5, 4, 3, 8, 6, 7, 5, 3, 4, 2, 5, 2]

packet_loss_multiple = [13, 13, 5, 8, 4, 3, 5, 8, 2, 4, 2, 4, 5, 8, 8, 0, 0, 2, 5, 4, 5, 4, 3, 8, 6, 7, 5, 3, 4, 2, 5,
                        2]

throughput_single = [1.09, 1.07, 1.02, 1.06, 1.05, 1.02, 1.07, 1.09, 1.02, 1.03, 1.07, 1.08, 1.07, 1.07, 1.04, 1.9,
                      1.5, 0.9,
                      1.05, 1.03, 1.02,
                      1.03, 1.02, 1.04, 1.02, 0.8, 0.6, 0.5, 0.9, 0.6, 0.3, 0.2]

throughput_multiple = [1.05, 1.07, 1.02, 1.06, 1.05, 1.02, 1.07, 1.09, 1.02, 1.03, 1.07, 1.08, 1.07, 1.07, 1.04, 1.9,
                        1.5, 1.6, 1.05, 1.03,
                        1.02, 1.03, 1.02, 1.04, 1.03, 1.03, 1.04, 1.05, 1.02, 1.3, 1.2, 1.1]


def print_graph(y1, y2, y_name):
    hosts = ["h" + str(i) for i in range(1, 33)]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=hosts,
                         y=y1,
                         name='Single Table',
                         marker_color='rgb(55, 83, 109)'
                         ))
    fig.add_trace(go.Bar(x=hosts,
                         y=y2,
                         name='Multiple Table',
                         marker_color='rgb(26, 118, 255)'
                         ))

    fig.update_layout(
        xaxis_tickfont_size=14,
        yaxis=dict(
            title=y_name,
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Host',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0.8,
            y=-0.3,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


print_graph(rtt_single, rtt_multiple, "RTT")
print_graph(jitter_single, jitter_multiple, "Jitter")
print_graph(throughput_single, throughput_multiple, "Throughput")