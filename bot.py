import os
import re
import yt_dlp
import asyncio
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import config
# --- Configuration ---
API_ID = config.API_ID  
API_HASH = config.API_HASH
BOT_TOKEN = config.BOT_TOKEN

app = Client("yt_downloader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

YT_REGEX = r"(https?://)?(www\.|m\.)?(youtube\.com|youtu\.be)/.+"

# --- Helper: Thumbnail Converter ---
def prepare_thumbnail(input_path):
    if not input_path or not os.path.exists(input_path):
        return None
    output_path = os.path.splitext(input_path)[0] + "_tg.jpg"
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGB")
            img.thumbnail((320, 320))
            img.save(output_path, "JPEG", quality=90)
        return output_path
    except:
        return None

# --- Core: Downloader ---
def download_video(url):
    ffmpeg_cmd = "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
    cookie_file = "cookies.txt"
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': True,
        'writethumbnail': True,
        'postprocessor_args': ['-c', 'copy', '-movflags', 'faststart'],
    }

    # Add Cookies if the file exists (Fixes "Sign in" error)
    if os.path.exists(cookie_file):
        ydl_opts['cookiefile'] = cookie_file

    # Only set ffmpeg_location if binary is in bot folder
    if os.path.exists(ffmpeg_cmd):
        ydl_opts['ffmpeg_location'] = os.path.abspath(ffmpeg_cmd)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info)
        
        if not os.path.exists(video_file):
            video_file = os.path.splitext(video_file)[0] + ".mp4"

        # Handle Thumbnails
        raw_thumb = None
        base = os.path.splitext(video_file)[0]
        for ext in ['.jpg', '.jpeg', '.webp', '.png']:
            if os.path.exists(base + ext):
                raw_thumb = base + ext
                break
        
        return {
            "file": video_file,
            "thumb": prepare_thumbnail(raw_thumb),
            "raw_thumb": raw_thumb,
            "title": info.get('title', 'Video'),
            "duration": int(info.get('duration', 0)),
            "width": info.get('width', 1280),
            "height": info.get('height', 720),
            "views": info.get('view_count', 0),
        }

# --- Shared Logic: Processing ---
async def process_video(message: Message, url: str, current=1, total=1):
    status_msg = f"🚀 **Processing link {current}/{total}...**"
    status = await message.reply(status_msg)
    data = None

    try:
        await status.edit(f"📥 **Downloading...**\n`{url}`")
        
        # Run in thread to keep bot responsive
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, download_video, url)

        await status.edit("📤 **Uploading to Telegram...**")

        caption = (
            f"🎵 **Title :** {data['title']}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👁 **Views :** {data['views']:,}\n"
            f"🔗 **Url :** [Watch On YouTube]({url})\n"
            f"⏱ **Duration :** {data['duration'] // 60}:{data['duration'] % 60:02d}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"**Downloaded By:** {message.from_user.mention}"
        )

        await message.reply_video(
            video=data['file'],
            caption=caption,
            thumb=data['thumb'],
            duration=data['duration'],
            width=data['width'],
            height=data['height'],
            supports_streaming=True
        )
        await status.delete()

    except Exception as e:
        await status.edit(f"❌ **Error on link {current}:**\n`{str(e)}`")
    
    finally:
        # Cleanup
        if data:
            if os.path.exists(data['file']): os.remove(data['file'])
            if data['thumb'] and os.path.exists(data['thumb']): os.remove(data['thumb'])
            if data['raw_thumb'] and os.path.exists(data['raw_thumb']): os.remove(data['raw_thumb'])

# --- Handlers ---
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "💎 **Vampire YT Downloader** 💎\n\n"
        "Send me a link or a .txt file with multiple links.\n\n"
        "👤 **Developer:** @Vampirex01",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Contact", url="https://t.me/Vampirex01")]])
    )

@app.on_message(filters.private & filters.text & filters.regex(YT_REGEX))
async def handle_text(client, message: Message):
    await process_video(message, message.text.strip())

@app.on_message(filters.private & filters.document)
async def handle_doc(client, message: Message):
    if message.document.file_name.endswith(".txt"):
        path = await message.download()
        with open(path, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
        os.remove(path)

        total_links = len(urls)
        if total_links == 0:
            return await message.reply("File is empty.")

        await message.reply(f"📂 Found **{total_links}** links. Starting batch download...")
        for i, url in enumerate(urls, 1):
            if re.match(YT_REGEX, url):
                await process_video(message, url, current=i, total=total_links)
            else:
                await message.reply(f"⚠️ Skipping invalid link at line {i}")


if __name__ == "__main__":
    print("Vampire Multi-Downloader is running...")
    app.run()