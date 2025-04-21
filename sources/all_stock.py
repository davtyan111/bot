from telegram import Update
from telegram.ext import ContextTypes
from sources.fastex import fetch_fastex_price_usdt as fetch_fastex_price_usdt
from sources.binance import get_usdt_price_Binance as fetch_binance_price
from sources.okx import fetch_okx_price as fetch_okx_price
from telegram import Update, ReplyKeyboardMarkup

stock_exchanges = {
    "Fastex": "/fastex",
    "Binance": "/binance",
    "Okx": "/okx",
    "All": "/all"
}

async def all_prices_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Checking USDT/AMD prices on all exchanges...")

    fastex_price = fetch_fastex_price_usdt()
    binance_price = fetch_binance_price()
    okx_price = fetch_okx_price()

    stock_keys = list(stock_exchanges.keys())

    reply = (
        f"📊 USDT/AMD Prices:\n"
        f"🔹 {stock_keys[0]}: {fastex_price}\n"
        f"🔸 {stock_keys[1]}: {binance_price}\n"
        f"⚫ {stock_keys[2]}: {okx_price}"
    )
    await update.message.reply_text(reply)
