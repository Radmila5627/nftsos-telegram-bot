import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
MINT_URL = os.getenv("MINT_URL", "https://nftsos-radmila.vercel.app")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"👋 Hello {user.mention_html()}!\n\n"
        f"🎉 Welcome to the NFTSOS* Telegram bot.\n"
        f"🛍️ Click below to mint your exclusive NFT and unlock special rewards!\n\n"
        f"👉 <a href='{MINT_URL}'>Mint NFTSOS*</a>\n\n"
        f"💎 You'll get 50% discount on future bracelet models!\n"
        f"✨ Powered by UO Alimdar - Blockchain Consulting."
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
