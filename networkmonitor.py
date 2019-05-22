from psutil import *
from collections import deque
import time
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

download = []
download.append(1)
upload = []
upload.append(1)
x = []
x.append(0)
external_css = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css', {
    'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T',
    'crossorigin': 'anonymous'
}]

app = dash.Dash(__name__, external_stylesheet=external_css)
app.layout = html.Div(
    [
        html.H1("Internet usage", className='h1'),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(id='graph-update', interval=1000, n_intervals=0),
    ]
)


def get_bytes():
    bytes_recv_last = net_io_counters().bytes_recv
    time_last = time.time()
    bytes_sent_last = net_io_counters().bytes_sent
    return[bytes_recv_last, time_last, bytes_sent_last]

@app.callback(Output('live-graph', 'figure'), [Input('graph-update', 'n_intervals')])
def animateGraph(n):

    b = get_bytes()
    
    bytes_recv_now = net_io_counters().bytes_recv
    bytes_sent_now = net_io_counters().bytes_sent
    time_now = time.time()
    
    kb_recv = ((bytes_recv_now-b[0])/(time_now-b[1]))/1024
    kb_sent = ((bytes_sent_now-b[2])/(time_now-b[1]))/1024

    upload.append(kb_sent)
    download.append(kb_recv)
    x.append(x[-1]+0.5)

    time_last = time_now
    bytes_recv_last = bytes_recv_now

    data = go.Scatter(
        y=list(download),
        line=go.scatter.Line(
            color='#42C4F7'
        ),
        mode='lines+markers',
        name="Download"
    )

    data2 = go.Scatter(
        y=list(upload),
        line=go.scatter.Line(
            color='#FF6961'
        ),
        mode='lines+markers',
        name="Upload"
    )

    layout = go.Layout(
        xaxis=dict(
            range=[min(x), max(x)],
        ),
        yaxis=dict(
            range=[min(download), max(download)],
            fixedrange=False
        )
    )

    return go.Figure(data=[data, data2], layout=layout)


if __name__ == '__main__':
    app.run_server(debug=True)
