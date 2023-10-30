# breaking down the software
# I. Dependencies
# II. Token information
# III. The Logic - COMMMANDS.1 + RESPONSES.2
# IV. Initlization of the Bot


# I. Dependencies + Libraries for the Bot
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# II. Token information (connecting Bot to Telegram server)
TOKEN: Final = '6423332775:AAHDiR78mAmkd-ijb5GWk8lgVMVyBtPH5nQ'
BOT_USERNAME: Final = '@the_menubot'


# III.1 Logic - COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("start command exmaple text")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("help command exmaple text")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom command example text")


# III.2 Logic - RESPONSES
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there'
        
    if 'how are you' in processed:
        return 'I am good'
        
    if 'i love python' in processed:
        return 'remember to subscribe'
        
        return 'I do not understand what you wrote'
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'chat':
        if BOT_USERNAME in text: 
             new_text: str = text.replace(BOT_USERNAME, '').strip()
             response: str = handle_response(new_text)
        else:
             return
    else: 
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
     print(f'Update {update} caused error {context.error}')


# IV. Initialization of Bot
if __name__ == '__main__':
    print('intializing menu bot')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
                     
    # ERRORS
    app.add_error_handler(error)

    # POLLS
    print('Polling...')
    app.run_polling(poll_interval=3)

