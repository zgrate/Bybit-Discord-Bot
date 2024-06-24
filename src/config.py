import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_TEST_MODE = os.environ.get('BYBIT_TEST_MODE', False)
BYBIT_API_KEY = os.environ.get('BYBIT_API_KEY', '')
BYBIT_API_SECRET = os.environ.get('BYBIT_API_SECRET', '')
BYBIT_SYMBOL = os.environ.get('BYBIT_SYMBOL', 'SOLUSDT')

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN', '')
DISCORD_CHANNEL_ID = int(os.environ.get('DISCORD_CHANNEL_ID', 0))

RSI_MIN_NOTIFICATION = int(os.environ.get('RSI_MIN_NOTIFICATION', 30))
RSI_MAX_NOTIFICATION = int(os.environ.get('RSI_MAX_NOTIFICATION', 70))

RSI_INTERVAL = int(os.environ.get('RSI_INTERVAL', 360))
RSI_PROCESS_LAST_TIMEFRAME_ENTRIES = int(os.environ.get('RSI_PROCESS_LAST_TIMEFRAME_ENTRIES', 24))

