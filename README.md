# alor_dev_auto_python
Generate python client for Alor Broker OpenAPI (alor.dev) from swagger

Файл alor_swagger.py основан на файле client.py из https://github.com/mechnotech/alor-api (Большое спасибо Евгению Шумилову, telegram: @mechnotech)

## Editor
1. Go to https://editor.swagger.io/
2. File -> Clear Editor
3. File -> Import Url 'https://alor.dev/rawdocs2/WarpOpenAPIv2.yml'

### Исправления для боевого использования
```
servers:
  - url: https://apidev.alor.ru
    description: Dev server
  - url: https://api.alor.ru
    description: Production server
``` 

- Удаляем все "WS" (из paths:)
- Добавляем кавычки, где нет
- Удаляем tags из всех команд (иначе генерируются в разные файлы)
- По желанию удаляем неиспользуемые схемы из schemas: (обозначаются восклицательным знаком и 'Definition was declared but never used in document')


### Исправления для команды "portfolios" - Получение списка серверов
```
description: Получение списка серверов по секциям «Валютный рынок», «Срочный рынок», «Фондовый рынок». В ответе в поле tradeServerCode содержится значение которое надо использовать
```
Заменяем components -> schemas -> servers_info на
```
    servers_info:
      type: array
      items:
        $ref: '#/components/schemas/portfolio_info'
    portfolio_info:
      type: array
      items:
        type: object
        properties:
          portfolio:
            type: string
            example: D39004
            description: Идентификатор клиентского портфеля
          tks:
            type: string
            example: L01-00000F00
          tradeServersInfo:
            type: array
            items:
              type: object
              properties:
                tradeServerCode:
                  type: string
                  example: TRADE
                  description: Код сервера
                addresses:
                  type: string
                  nullable: true
                  example: null
                type:
                  type: string
                  nullable: true
                  example: null
                contracts:
                  type: string
                  example: РЦБ
                market:
                  type: string
                  nullable: true
                  example: null
                accountNum:
                  type: string
                  nullable: true
                  example: null
```

### Генерация клиента
1. File - Save as yaml (на всякий случай)
2. Generate client -> Python
3. Скачиваем, разархивируем
4. Устанавливаем зависимости из requirements.txt (pip install -r requirements.txt)
5. Устанавливаем requests (pip install requests)
6. Копируем/переносим папку "swagger_client" в папку со своим проектом

## Использование
1. Добавляем файл alor_swagger.py в папку со своим проектом
2. В файле alor_swagger.py настраиваем
```
LOGGING = True # Записывать ошибки в debug.log
DEVMODE = True # в режиме разработчика, подключения идут к тествовым серверам
TTL_JWT_TOKEN = 1740 # Время жизни jwt-токена в секундах
```
3. В запускаемом файле своего проекта
```
import alor_swagger
alor = alor_swagger.Api(username='P0*****', refresh='***')
```
4. Примеры вызовов
```
alor._get_jwt_token()   # обновление jwt токена
alor._bearer()          # проверка jwt на срок годности и возвращение текущей Bearer строки

alor.client.dev_user_portfolio(username=alor.username) # получение списки портфелей/серверов по рынкам
```
5. Все команды API описаны и находятся в swagger_client -> api -> default_api.py (также отображаются в некоторых IDE)
6. Описание полезных атрибутов
```
alor._random_order_id     # уникальная строка для использования в ордерах
alor.username             # логин, который указывается при инициализации
alor.refresh_token        # рефреш токен
alor.jwt_token            # текущий jwt токен
alor.bearer               # текущая Bearer строка для авторизационных заголовков
alor.jwt_token_issued_at  # примерный timestamp выпуска jwt

alor.fx_portfolio         # портфель на валютном рынке
alor.fx_tks               # ткс на валютном рынке
alor.fx_tradeServerCode   # сервер для валютного рынка

alor.forts_portfolio      # портфель на срочном рынке
alor.forts_tks            # ткс на срочном рынке
alor.forts_futures_tradeServerCode  # сервер для фьючерсов
alor.forts_options_tradeServerCode  # сервер для опционов

alor.fund_portfolio       # портфель на фондовом рынке
alor.fund_tks             # ткс на фондовом рынке
alor.fund_moex_tradeServerCode      # сервер для фондового рынка мосбиржи
alor.fund_spbx_tradeServerCode      # сервер для фондового рынка СПБ биржи
```
