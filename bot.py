import telebot
import yt_dlp
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔗 Link bhejo, main video download karke de dunga")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text.strip()

    # Shorts URL fix
    if "youtube.com/shorts/" in url:
        video_id = url.split("/")[-1].split("?")[0]
        url = f"https://www.youtube.com/watch?v={video_id}"

    bot.reply_to(message, "⏳ Download ho rahi hai...")

    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'mp4',
        'noplaylist': True,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as f:
            bot.send_video(message.chat.id, f)

        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, "❌ Download fail. Dusri link try karo")

bot.infinity_polling()
