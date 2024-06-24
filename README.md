# Bybit Discord Bot

Functional requirements Write a Discord bot in Python that

    Constantly fetches spot K-line data for SOL/USDT pair from Bybit
    Calculates RSI (relative strength index) for this symbol based on closing price
    Sends a text message to Discord channel if the calculated RSI value is over 70 or below 30
    Use the 1H (1 hour) time frame

Non-functional requirements

    The code should be readable and clean but is not expected to be production-ready nor fully covered with tests.
    Delay between the bar close and notification should be less than 10 seconds
    RSI should be calculated using a technical analysis library of your choice
    Solution should run inside the Docker container and include corresponding Dockerfile
    Solution is expected in form of github repository that includes readme instructions on how to run it


Starting bot:
1. Copy example.env and rename it to .env
2. Fill up the enviromental values. There is no need to specify API keys for Bybit as K-Line can be fetched publicly
3. Start app using ``docker compose build && docker compose up -d``
