from logger import logger
from telegram.error import BadRequest
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from funct import *
from cons import *
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CallbackQueryHandler(pattern='ru_change', callback=ru_change))
dis.add_handler(CallbackQueryHandler(pattern='uz_change', callback=uz_change))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(CallbackQueryHandler(pattern='xlsx', callback=xlsx))
dis.add_handler(CallbackQueryHandler(pattern='delete_f', callback=delete_f))
dis.add_handler(CallbackQueryHandler(pattern='user_list', callback=user_list))

dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))
dis.add_handler(MessageHandler(Filters.photo, adm))
dis.add_handler(MessageHandler(Filters.video, adm_v))
def error_callback(bot, update, error):
    try:
        raise error
    except BadRequest:
        # handle malformed requests - read more below!
        print('Same message')


def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))

    upd.dispatcher.logger.addFilter(
        (lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))

upd.start_polling(drop_pending_updates=True)
