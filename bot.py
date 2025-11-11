from telegram.ext import Application, CommandHandler
import os

# احصل على التوكن من متغير البيئة
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# الدوال الأساسية
async def start(update, context):
    await update.message.reply_text('مرحباً! البوت يعمل بنجاح 🎉')

async def help(update, context):
    await update.message.reply_text('أنا بوت مساعد، استخدم /start لبدء المحادثة')

def main():
    # 1. إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()
    
    # 2. إضافة الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    # 3. بدء التشغيل
    print("🚀 البوت يعمل...")
    application.run_polling()

if __name__ == '__main__':
    main()
