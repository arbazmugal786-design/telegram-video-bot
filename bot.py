import telebot
import yt_dlp
import os

BOT_TOKEN = "8334828200:AAGePTwprzsuN0uvvHZnvIa3YYF8WzkLtRw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Link bhejo, main video download karke de dunga! 🚀")

@bot.message_handler(func=lambda msg: True)
def download_video(message):
    url = message.text

    bot.reply_to(message, "⏳ Video download ho rahi hai, please wait...")

    try:
        ydl_opts = {
            'outtmpl': 'video.mp4',
            'format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open("video.mp4", "rb") as video:
            bot.send_video(message.chat.id, video)

        os.remove("video.mp4")

    except Exception as e:
        bot.reply_to(message, "❌ Error: Video download nahi ho payi.\nLink sahi bhejo ya dusri link try karo.")

bot.polling()
