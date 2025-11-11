from telegram.ext import Application, CommandHandler
import os
import logging

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# تحقق من وجود التوكن
if not TOKEN:
    logger.error("❌ لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")
    exit(1)

async def start(update, context):
    """يرسل رسالة ترحيب عندما يتم استخدام الأمر /start"""
    user = update.effective_user
    await update.message.reply_text(
        f'مرحباً {user.first_name}! 🎉\n'
        f'البوت يعمل بنجاح مع الإصدار الحديث'
    )

async def help_command(update, context):
    """يرسل رسالة المساعدة عندما يتم استخدام الأمر /help"""
    await update.message.reply_text(
        '📋 الأوامر المتاحة:\n'
        '/start - بدء التشغيل\n'
        '/help - عرض هذه الرسالة'
    )

def main():
    try:
        # إنشاء التطبيق باستخدام النمط الحديث
        application = Application.builder().token(TOKEN).build()
        
        # إضافة معالجات الأوامر
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        
        logger.info("🚀 بدء تشغيل البوت...")
        print("✅ البوت يعمل بنجاح!")
        
        # بدء الاستطلاع
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ خطأ في التشغيل: {e}")
        exit(1)

if __name__ == '__main__':
    main()
