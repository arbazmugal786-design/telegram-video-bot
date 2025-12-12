import os
import traceback
import yt_dlp
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("8334828200:AAGePTwprzsuN0uvvHZnvIa3YYF8WzkLtRw")

def download_video(url):
    try:
        # Output path
        out = "video.mp4"

        ydl_opts = {
            "format": "mp4",
            "outtmpl": out,
            "quiet": True,
            "no_warnings": True,
            "retries": 3,
            "ignoreerrors": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return out if os.path.exists(out) else None

    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return None

def handle_message(update, context):
    url = update.message.text

    update.message.reply_text("⏳ Video download ho rahi hai, please wait...")

    file = download_video(url)

    if file:
        update.message.reply_video(video=open(file, "rb"))
        os.remove(file)
    else:
        update.message.reply_text("❌ Error: Video download nahi ho payi. Sahi link bhejo!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
