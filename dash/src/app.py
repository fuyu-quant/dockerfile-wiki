# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = sns.load_dataset('tips')
use_data = df[['total_bill','size','time','tip']]
use_data = pd.get_dummies(use_data, drop_first=True)

X = use_data[['total_bill','size','time_Dinner']]
Y = use_data[['tip']]


clf = LinearRegression()
clf.fit(X, Y)


#　表示するグラフの作成
import plotly.graph_objects as go
from plotly.subplots import make_subplots

tip_plots = make_subplots(rows = 1, cols = 3, start_cell = 'bottom-left')
tip_plots.add_trace(go.Box(x = df['time'], y= df['tip'], name = 'time vs tip'), row = 1, col = 1)
tip_plots.add_trace(go.Scatter(x = df['total_bill'], y= df['tip'],mode = 'markers', name = 'total_bill vs tip'), row = 1, col = 2)
tip_plots.add_trace(go.Scatter(x = df['size'], y= df['tip'],mode = 'markers', name = 'size vs tip'), row = 1, col = 3)
tip_plots.update_layout(
    xaxis_title_text = 'Time (Lunch or Dinner)',
    yaxis_title_text = 'Tip ($)'
)
tip_plots.update_layout(
    xaxis2_title_text='Total bill ($)',
    yaxis2_title_text='Tip ($)'
)
tip_plots.update_layout(
    xaxis3_title_text='Total bill (人)',
    yaxis3_title_text='Tip ($)'
)

#　アプリ部分
import dash
from dash import html
from dash import dcc
from dash import dash_table
from dash.dependencies import Input, Output, State


app = dash.Dash()

app.layout = html.Div([
    html.H1('チップの額を予測するアプリです!', style = {"textAlign":"center"}),
    html.H2('まずは分析に使うデータを見てみましょう!'),
    # dataframeの可視化
    dash_table.DataTable(
        style_cell = {'textAlign':'center','width':'150px'},
        fill_width = False,  # 幅は上で設定したのでFalse
        fixed_rows = {'headers':True},  # ヘッダーの固定
        page_size = 10, #何行出すか
        filter_action = 'native',
        sort_action = 'native',
        columns = [{'name':col, 'id':col} for col in df.columns],
        data = df.to_dict('records')
    ),
    html.P('モデリングに使うデータは{}件ですよ!'.format(len(df))),
    html.H2('次はグラフを見てみましょう!(グラフの要素は固定)'),
    dcc.Graph(
        id='graph',
        figure=tip_plots,
        style={}
    ),
    html.H2('予測用のデータをインプットしてみましょう!'),
    dcc.Input(
        id = 'total_bill',
        placeholder='total bill ここに値を入れてください', # 空白の時の文字
        type = 'text',
        style = {'width':'20%'},
        value = '' # 何を入れておくか
    ),
    dcc.Input(
        id = 'size',
        placeholder='size ここに値を入れてください', # 空白の時の文字
        type = 'text',
        style = {'width':'20%'},
        value = '' # 何を入れておくか
    ),
    dcc.RadioItems(
        id = 'time',
        options=[
            {'label':'ランチ','value':'Lunch'},
            {'label':'ディナー','value':'Dinner'}
        ],
        value = 'Lunch',
        labelStyle={'display':'inline-block'}
    ),
    html.Button(
        id='submit-button',
        n_clicks=0,  # クリックされたら発動するような設定
        children='Submit'
    ),
    html.H2('チップの予測額はいくらかな?'),
    html.Div(
        id='output-pred',
        style={'textAlign':'center','fontSize':'30', 'color':'red'}
    )
])

@app.callback(
    Output('output-pred','children'),
    Input('submit-button','n_clicks'),
    [State('total_bill','value'),
    State('size','value'),
    State('time','value')]
)
def prediction(n_clicks, total_bill, size, time):
    if time == 'Lunch':
        dinner01 = 0
    else:
        dinner01 = 1

    if (total_bill and size):
        value_df = pd.DataFrame([], columns = ['total_bill','Size', 'Dinner flag'])
        record = pd.Series([total_bill, size, dinner01], index = value_df.columns, dtype='float64')
        value_df = value_df.append(record, ignore_index = True)
        Y_pred = clf.predict(value_df)

        return_text = 'チップ額はおそらく' + str('{:.2g}'.format(Y_pred[0,0])) + 'ドルくらいでしょう!'
        return return_text

    else:
        return 'ちゃんとデータを入力してね!'

if __name__=='__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)