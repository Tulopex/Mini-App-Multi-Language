const TelegramBot = require('node-telegram-bot-api');

const token = '7491358509:AAFduYaD1INiYUDZWWbF7GSPCdgJNXTkVrY';

const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const webAppUrl = 'https://www.youtube.com';
    
    const keyboard = {
        inline_keyboard: [
            [
                {
                    text: 'Запустить',
                    web_app: { url: webAppUrl }
                }
            ]
        ]
    };

    bot.sendMessage(chatId, 'Добро пожаловать!\nЭто Mini App внутри Telegram', {
        reply_markup: keyboard
    });
});