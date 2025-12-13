import telebot
import yt_dlp
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Link bhejo, main video download karke dunga")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    bot.reply_to(message, "⏳ Download ho rahi hai...")

    try:
        ydl_opts = {
            'outtmpl': 'video.%(ext)s',
            'format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as f:
            bot.send_video(message.chat.id, f)

        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, "❌ Download fail. Dusri link try karo")

bot.infinity_polling()
