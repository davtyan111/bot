from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from sources.fastex import fetch_fastex_price_usdt, fetch_fastex_price_BTC
from sources.binance import get_usdt_price_Binance, get_btc_price_Binance
from sources.okx import fetch_okx_price
from sources.all_stock import all_prices_command
from webdriver_manager.chrome import ChromeDriverManager 

# Telegram /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["USDT 💵", "BTC 🪙"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 *Welcome to Crypto Change Bot* 💱\n\n"
        "I’m here to help you check live exchange rates for *USDT/AMD* and *BTC/USDT* across top platforms.\n\n"
        "💡 What you can do:\n"
        "• Check real-time crypto prices 📊\n"
        "• Compare rates on Fastex, Binance, and OKX ⚖️\n"
        "• Use buttons below or type commands manually\n\n"
        "🌍 *First, choose the cryptocurrency you want to check:*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Handles USDT or BTC selection
async def handle_coin_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin = update.message.text.strip().lower()

    if "usdt" in coin:
        context.user_data["coin"] = "usdt"
        keyboard = [["fastex", "binance", "okx"]]
    elif "btc" in coin:
        context.user_data["coin"] = "btc"
        keyboard = [["fastex", "binance"]]
    else:
        await update.message.reply_text("❗ Please choose *USDT* or *BTC* using the buttons.")
        return

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        f"✅ You chose *{coin.upper()}*. Now choose an exchange:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Handles exchange choice dynamically
async def handle_exchange_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    exchange = update.message.text.strip().lower()
    coin = context.user_data.get("coin", "").lower()

    if coin == "usdt":
        if exchange == "fastex":
            await fastex_command(update, context)
        elif exchange == "binance":
            await binance_command(update, context)
        elif exchange == "okx":
            await okx_command(update, context)
        else:
            await update.message.reply_text("❗ Invalid exchange for USDT.")
    elif coin == "btc":
        if exchange == "fastex":
            await bitcoin_command(update, context)
        elif exchange == "binance":
            await binance_command_btc(update, context)
        else:
            await update.message.reply_text("❗ Invalid exchange for BTC.")
    else:
        await update.message.reply_text("❗ Please select a coin first using /start.")

# Exchange command functions
async def fastex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Checking USDT/AMD price in Fastex...")
    price = fetch_fastex_price_usdt()
    await update.message.reply_text(f"📊 USDT/AMD Price\n🔹Fastex: {price}")

async def binance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Checking USDT/AMD price in Binance...")
    price = get_usdt_price_Binance()
    await update.message.reply_text(f"📊 USDT/AMD Price\n🔸Binance: {price}")

async def binance_command_btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Checking BTC/USDT price in Binance...")
    price = get_btc_price_Binance()
    await update.message.reply_text(f"₿ BTC/USDT Price\n🔸Binance: {price}")

async def okx_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Checking USDT/AMD price in OKX...")
    price = fetch_okx_price()
    await update.message.reply_text(f"📊 USDT/AMD Price\n⚫OKX: {price}")

async def bitcoin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Checking BTC/USDT price in Fastex...")
    price = fetch_fastex_price_BTC()
    await update.message.reply_text(f"₿ BTC/USDT Price\n🔹Fastex: {price}")
