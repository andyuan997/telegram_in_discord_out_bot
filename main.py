from telegram.ext import Updater, MessageHandler, Filters
import discord
import os
import asyncio
import threading

def run_telegram_bot():
    TOKEN = '6898476769:AAGb2pZiqgkvLqh_TsZTRraPg8ii-ylVEuo'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    # updater.idle()

def run_discord_bot():
    token = 'MTE4NzI0OTQ0NDQ5Njg4MzczMg.GE-_kY.su09d5ZtJHt0Ll9H2Wi2Trz6eGhbz5ZT8LaxeA'
    client.run(token)

def handle_message(update, context):
    message = update.message.text
    chat_id = update.message.chat_id
    print(f"Received message '{message}' in chat {chat_id}")

    # 將訊息寫入文件
    with open('telegram_messages.txt', 'a') as file:
        file.write(f"{message}\n")

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # 啟動消息發送任務
    client.loop.create_task(send_telegram_messages())

async def send_telegram_messages():
    await client.wait_until_ready()
    #channel = client.get_channel(YOUR_DISCORD_CHANNEL_ID)  # 替換為您的頻道ID
    channel = client.get_channel(1187106541950738464)  # 替換為您的頻道ID
    while not client.is_closed():
        # 檢查是否有新消息
        if os.path.exists('telegram_messages.txt'):
            with open('telegram_messages.txt', 'r') as file:
                messages = file.readlines()
            with open('telegram_messages.txt', 'w') as file:
                file.truncate(0)  # 清空文件

            # 在Discord頻道中發送消息
            for message in messages:
                await channel.send(message.strip())

        await asyncio.sleep(10)  # 每10秒檢查一次

if __name__ == '__main__':
    telegram_thread = threading.Thread(target=run_telegram_bot)
    discord_thread = threading.Thread(target=run_discord_bot)

    telegram_thread.start()
    discord_thread.start()

    telegram_thread.join()
    discord_thread.join()
