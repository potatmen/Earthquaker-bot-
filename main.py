import telebot
from find_nearest_place import nearest
from coordinates_processing import check, cords
bot = telebot.TeleBot("2062779263:AAE7_XjRInzZhcpZKscbwk2UxCGIZvrMfpk")
user_id = 0
@bot.message_handler(content_types=["text"])
def greetings(message):
    global user_id
    user_id = message.chat.id
    bot.send_message(user_id,"Hello, I'm earthquaker bot. I can determine the nearest earthquake to you during the previous 30 days. Write /start.")
    bot.register_next_step_handler(message,get_coordinates)
def get_coordinates(message):
    if message.text == "/start":
        bot.send_message(user_id,"Now I need your coordinates. You can use <a href='https://www.google.com/maps'>Google Maps</a>. Enter the location, or select and hold to drop a pin on the map of the location you want the coordinates for. Then, send me these coordinates.",parse_mode="HTML")
        bot.register_next_step_handler(message,process_coordinates)
    else:
        bot.send_message(user_id,"Please, write /start to start.")
        bot.register_next_step_handler(message,get_coordinates)
def process_coordinates(message):
    if check(message.text):
        user_cord = cords(message.text)
        
        bot.send_message(user_id,nearest(user_cord[0],user_cord[1]))
    else:
        bot.send_message(user_id,"You entered the coordinates incorrectly. Try one more time.")
        bot.register_next_step_handler(message,process_coordinates)

bot.polling(none_stop=True,interval=0)
     
