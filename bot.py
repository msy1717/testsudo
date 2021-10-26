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
    amaan=king[7:]
    link_match = match(r"\bhttps?://.*\.\S+", amaan)
    if not link_match:
        await event.edit("I need a valid link to take screenshots from.")
        return
    link = link_match.group()
    await .event.edit("Processing ...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome((ChromeDriverManager().install()),chrome_options=chrome_options)
    driver.get(link)
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
        "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
        "document.documentElement.offsetWidth);"
    )
    driver.set_window_size(width + 125, height + 125)
    wait_for = height / 1000
    await message.edit(
        f"Generating screenshot of the page..."
        f"\nHeight of page = {height}px"
        f"\nWidth of page = {width}px"
        f"\nWaiting ({int(wait_for)}s) for the page to load."
    )
    await asyncio.sleep(int(wait_for))
    im_png = driver.get_screenshot_as_png()
    driver.close()
    message_id = message.message.id
    reply = await message.get_reply_message()
    if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
    file_path = os.path.join(Config.TEMP_DOWNLOAD_DIRECTORY , "webss.png")
    async with aiofiles.open(file_path, "wb") as out_file:
        await out_file.write(im_png)
    await asyncio.gather(
        message.delete(),
        message.client.send_file(
            message.chat_id,
            file_path,
            caption=link,
            force_document=False,
            reply_to=message_id,
        ),
    )
    os.remove(file_path)
    driver.quit()

logging.info("\n\nBot has started.\n(c) @Godmrunal")

bot.run_until_disconnected()
