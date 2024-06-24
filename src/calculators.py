import pandas as pd


def process_incoming_kline_data(kline_data, rsi_for_last_entires=14):
    df = pd.DataFrame(data=kline_data['result']['list'],
                      columns=["startTime", "openPrice", "highPrice", "lowPrice", "closePrice", "volume", "turnover"],
                      dtype=float)

    data = df.loc[:, ['closePrice']]
    column = data[['closePrice']]
    data['change'] = column - column.shift(1)

    data = data.tail(rsi_for_last_entires)

    data['gain'] = data['change']
    data['loss'] = data['change']

    data.loc[data['gain'] < 0, 'gain'] = 0
    data.loc[data['loss'] > 0, 'loss'] = 0
    data['loss'] = data['loss'] * -1

    avg_gain = data['gain'].mean()
    avg_loss = data['loss'].mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
