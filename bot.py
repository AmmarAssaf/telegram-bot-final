import os
from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text('🎉 البوت يعمل! السلام عليكم')

def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN', '8415474087:AAEDtwjvgogXfvpMzARe875svIEkSSDdNXk')
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 البوت يعمل!")
    app.run_polling()

if __name__ == '__main__':
    main()
