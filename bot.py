# < (c) 2021 @Godmrunal >

import logging
from os import remove
import asyncio

import os

from re import match

import aiofiles

from selenium import webdriver









from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import requests
from telethon import Button, TelegramClient, events
from htmlwebshot import WebShot
from telethon.errors.rpcerrorlist import PhotoInvalidDimensionsError


BOT_TOKEN = '2001104701:AAGUr8Vjt1s2UPuFSYMosFZIo0EeDCHLqwE'

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bot = TelegramClient(None, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
    bot_token=("2001104701:AAGUr8Vjt1s2UPuFSYMosFZIo0EeDCHLqwE")
)

logging.info("Starting bot...")


@bot.on(events.NewMessage(incoming=True, pattern="^/start"))
async def start_(event):
    await event.reply(
        "Hi {}!\nI am a simple bot. \n\n**Usage:** This bot will help to start first bot in python!".format(
            (await bot.get_entity(event.sender_id)).first_name
        ),
        buttons=[
            [
                Button.url("Repo", url="https://github.com/msy1717/startBot"),
                Button.url(
                    "Developer", url="https://t.me/Godmrunal"
                ),
            ],
            [Button.url("Channel", url="https://t.me/Botz_Official")],
        ],
    )

@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def webss(event):
    king= event.text
    await event.edit(king)


logging.info("\n\nBot has started.\n(c) @Godmrunal")

bot.run_until_disconnected()
