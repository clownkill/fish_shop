# fish_shop
 
Telegram-бот для продажи рыбы (@FishStoreDvmnBot)

## Как установить

* Python3 должен быть установлен
* Скопировать репозиторий к себе на компьютер:
```
https://github.com/clownkill/fish_shop
```
* Установите зависимости:
```
pip install -r requrirements
```

## Переменные окружения

```
CLIENT_ID=[ID для доступа CMS moltin.com]
TELEGRAM_TOKEN=[Telegram-токен для достуба к боту]
REDIS_HOST=[Хост для базы данных Redix]
REDIS_PORT=[Порт базы данных Redis]
REDIS_DB_PSWD=[Пароль к базе данных Redis]
```

## Как запустить

* Для запуска telegram-бота необходимо выполнить:
```
python tg_bot.py
```

## Деплой

Для деплоя проекта необходимо воспользоваться инструкцией на [heroku](https://devcenter.heroku.com/categories/deployment).

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
