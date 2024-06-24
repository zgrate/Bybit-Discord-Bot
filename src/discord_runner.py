import discord
from discord.ext import tasks

from bybit_connector import create_kline_stream_websocket, get_kline_data
from calculators import process_incoming_kline_data
from config import DISCORD_CHANNEL_ID, DISCORD_BOT_TOKEN, RSI_MAX_NOTIFICATION, RSI_MIN_NOTIFICATION


class MainTaskDiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mark_kline_to_process = False

    def handle_kline_data(self, message):
        for d in message['data']:
            if d['confirm']:
                self.mark_kline_to_process = True
                print("Got a confirmation. processing....")

    async def setup_hook(self) -> None:
        create_kline_stream_websocket(self.handle_kline_data)
        print("STARTING TASK....")
        self.main_task_loop.start()

    async def on_ready(self):
        print(f'Bot connected {self.user} ID: {self.user.id}')

    @tasks.loop(seconds=1)
    async def main_task_loop(self):
        if self.mark_kline_to_process:
            rsi = process_incoming_kline_data(get_kline_data())
            if rsi < RSI_MIN_NOTIFICATION or rsi > RSI_MAX_NOTIFICATION:
                channel = self.get_channel(DISCORD_CHANNEL_ID)
                await channel.send(f"RSI reached notification threshold! It is now {rsi}")

            self.mark_kline_to_process = False

    @main_task_loop.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()



def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = MainTaskDiscordClient(intents=intents)
    try:
        client.run(DISCORD_BOT_TOKEN)
    except KeyboardInterrupt:
        client.close()
        return client

    return client