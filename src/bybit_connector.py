from pybit.unified_trading import WebSocket, HTTP

from config import BYBIT_TEST_MODE, RSI_INTERVAL, BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_SYMBOL


def create_kline_stream_websocket(handle):
    ws = WebSocket(
        testnet=BYBIT_TEST_MODE,
        channel_type="linear",
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )

    ws.kline_stream(RSI_INTERVAL, BYBIT_SYMBOL, handle)


def create_client():
    #We don't need api keys to access it, but futureproof
    return HTTP(
        testnet=BYBIT_TEST_MODE,
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )


def get_kline_data(interval=RSI_INTERVAL):
    client = create_client()
    kline_data = client.get_kline(symbol=BYBIT_SYMBOL, interval=interval)
    return kline_data
