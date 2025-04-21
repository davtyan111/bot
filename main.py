from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)
from bot.handlers import (
    start_command,
    handle_coin_choice,
    handle_exchange_choice,
    fastex_command,
    binance_command,
    okx_command,
    bitcoin_command,
    binance_command_btc,
    all_prices_command,
)
from bot.config import TELEGRAM_TOKEN

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Slash commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("fastex", fastex_command))
    app.add_handler(CommandHandler("binance", binance_command))
    app.add_handler(CommandHandler("binance_btc", binance_command_btc))
    app.add_handler(CommandHandler("bitcoin", bitcoin_command))
    app.add_handler(CommandHandler("okx", okx_command))
    app.add_handler(CommandHandler("all", all_prices_command))

    # Handles USDT / BTC choice
    app.add_handler(MessageHandler(filters.Regex("(?i)^usdt.*|btc.*"), handle_coin_choice))


    # Handles selected exchanges
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_exchange_choice))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
