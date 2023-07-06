

# # Токени двох ботів
# seller_bot_token = '6362111511:AAEh7v9VaSc7LpNE0NM8jKBPITSNuh5RfUg'
# buyer_bot_token = '6329851632:AAFS3xxEIg4I0X_eDUKfMh_pvhmwzOOPLYw'

# # Функція-обробник повідомлень від продавця
# def handle_seller_message(update: Update, context):
#     message = update.message
#     if message is not None and message.text is not None:
#         # Отримати текст повідомлення
#         text = message.text
        
#         # Відправити повідомлення від продавця покупцю
#         send_message(buyer_bot_token, text)

# # Функція-обробник повідомлень від покупця
# def handle_buyer_message(update: Update, context):
#     message = update.message
#     if message is not None and message.text is not None:
#         # Отримати текст повідомлення
#         text = message.text
        
#         # Відправити повідомлення від покупця продавцю
#         send_message(seller_bot_token, text)

# # Відправити повідомлення від одного бота до іншого
# def send_message(bot_token, text):
#     bot = Bot(token=bot_token)
#     bot.send_message(chat_id='@target_chat_id', text=text)

# def main():
#     # Налаштування журналування
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
#     # Створення об'єкту продавця
#     seller_bot = Bot(token=seller_bot_token)
    
#     # Створення об'єкту покупця
#     buyer_bot = Bot(token=buyer_bot_token)
    
#     # Створення об'єкту для отримання оновлень від продавця
#     seller_updater = Updater(bot=seller_bot, use_context=True)
    
#     # Створення об'єкту для отримання оновлень від покупця
#     buyer_updater = Updater(bot=buyer_bot, use_context=True)
    
#     # Додавання обробників повідомлень для продавця та покупця
#     seller_updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_seller_message))
#     buyer_updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_buyer_message))
    
#     # Запуск отримання оновлень продавця
#     seller_updater.start_polling()
    
#     # Запуск отримання оновлень покупця
#     buyer_updater.start_polling()
   
