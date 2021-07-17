# alor_dev_auto_python
Generate python client for Alor Broker OpenAPI (alor.dev) from swagger

## Editor
1. Go to https://editor.swagger.io/
2. File -> Clear Editor
3. File -> Import Url 'https://alor.dev/rawdocs2/WarpOpenAPIv2.yml'

### Исправления для боевого использования
```
servers:
  - url: https://api.alor.ru
    description: Production server
``` 

- Удаляем все "WS" (из paths:)
- Добавляем кавычки, где нет
- Удаляем tags из всех команд (иначе генерируются в разные файлы)


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
1. Generate client -> Python
2. Скачиваем, разархивируем
3. Устанавливаем зависимости из requirements.txt (pip install -r requirements.txt)
4. Устанавливаем requests (pip install requests)
5. Копируем/переносим папку "swagger_client" в папку со своим проектом

## Использование
1. Добавляем файл alor_swagger.py в папку со своим проектом
2. В запускаемом файле 
```
import alor_swagger
alor = alor_swagger.Api(username='P0*****', refresh='***')
```
3. Пример вызова
```
alor.client.dev_user_portfolio(username='P0*****')
```
4. Все команды API описаны и находятся в swagger_client -> api -> default_api.py
