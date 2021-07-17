# coding: utf-8

# flake8: noqa
"""
    Alor OpenAPI V2

    <small>Swagger-документация для API v1 доступна по ссылке&#58; <a href=\"https://alor.dev/rawdocs/WarpOpenApi3.yml\">https://alor.dev/rawdocs/WarpOpenApi3.yml</a></small><br><br> API для работы с торговой системой АЛОР Брокер. Предоставляет интерфейсы для выставления заявок и получения биржевой информации.  Данные для неавторизованных запросов предоставляются с 15-минутной задержкой, для авторизованных - без задержек.   Публичная биржевая информация может быть получена через HTTP(S) API, а также доступна через однократно установленное WebSocket соединение. <br> **Внимание!** WebSocket соединения могут и будут разрываться *(например, если клиент не успевает обрабатывать сообщения и на стороне API в буфере накопится более 5000 событий)*. <br> Во внешнем ПО необходимо предусмотреть механизмы переподключения и переподписки (при необходимости)! <br> <br>  В OpenAPI V2 \"Санкт-Петербургская биржа\" (SPBX) еще находится в процессе разработки. Доступно получение рыночных данных *(marketdata, md)*. Заявки на SPBX в V2 пока недоступны. В V1 торговый функционал для SPBX доступен.  <h4> Доступные типы данных </h4>  * Все сделки  * Все заявки  * Информация по инструментам  * Котировки  * Биржевые стаканы  * Исторические данные  * Позиции  * Информация о клиенте  <h4>Поддерживаемые виды заявок</h4>  * рыночные  * лимитные  * стоп-лосс  * тейк-профит  * стоп-лосс лимит  * тейк-профит лимит  <h4>    Ограничения по частоте запросов     </h4> <p>На текущий момент ограничений по количеству запросов в минуту или WebSocket-подписок нет. <br/> Сервер может обрабатывать \"тяжелые\" запросы (пример - история за все время) и запросы без авторизации с меньшим приоритетом. <br/> АЛОР оставляет за собой право на ограничение частоты запросов, если это будет необходимо для стабильной работы системы. <br/> <br/></p>   <h2> Авторизация </h2>  <h4>OAuth</h4>  <b>Внимание!</b>   JWT и refresh token — равносильны логину и паролю. Их нужно скрывать от публичного доступа.  <h4>Для разработчиков сторонних приложений, в которых торговлю будут вести их пользователи.</h4>  Мы предоставляем сервис для авторизации сторониих приложений по стандарту OAuth 2.0. С примером приложения, использующего OAuth сервис для авторизации пользователей можно ознакомиться в разделе  <a href=\"/examples\">Примеры</a>.  Список разрешений (scopes), которые могут быть выданы приложению: <table>   <tr>     <td><b>OrdersRead</b></td>     <td>Чтение выставленных заявок</td>   </tr>   <tr>     <td><b>OrdersCreate</b></td>     <td>Выставление заявок</td>   </tr>   <tr>     <td><b>Trades</b></td>     <td>Чтение совершенных сделок</td>   </tr>   <tr>     <td><b>Personal</b></td>     <td>Персональная информация: ФИО, почта и т.п.</td>   </tr>   <tr>     <td><b>Stats</b></td>     <td>Статистика: прибыль, средние цены и т.п.</td>   </tr> </table>  <h4>Для ведения операций от своего имени</h4>  Выписать себе <b>refresh token</b> для ведения операций от своего имени [можно здесь](https://alor.dev/open-api-tokens).  <h2>Краткое описание работы с авторизацией</h2>  Чтобы выполнить авторизованный запрос, добавьте в запрос заголовок с именем \"Authorization\" и значением, состоящим из префикса `\"Bearer \"` и валидного JWT токена.  Срок жизни JWT короткий: это сделано для безопасности.  Для большинства вариантов использования API мы рекоммендуем использовать механизм  <b>refresh token</b> .  Механизм  <b>refresh token</b>  позволяет получать JWT с новым сроком жизни. Для этого отправьте POST запрос на адрес `https://oauthdev.alor.ru/refresh?token={refreshToken}` *(игровой контур)* или `https://oauth.alor.ru/refresh?token={refreshToken}` *(боевой контур)*. Если у  <b>refresh token</b>  не истек срок жизни и не он не был отозван, то в теле ответа в поле AccessToken вернётся свежий JWT токен.   Срок жизни  <b>refresh token</b>, получаемого обычным способом — 1 месяц.   Срок жизни  <b>refresh token</b>, получаемого самостоятельным выписыванием — год.  | |-  > Если мы для вас не завели портфели для ведения торговли в игровом контуре, оставьте заявку на <a href=\"mailto:openapi@alor.ru\">openapi@alor.ru</a> или свяжитесь с нами в [телеграме](https://tgmssg.ru/AlorOpenAPI).  </br></br> Игровой контур: `https://apidev.alor.ru`  Боевой контур: `https://api.alor.ru`   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: openapi@alor.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.alltrade import Alltrade
from swagger_client.models.alltrades import Alltrades
from swagger_client.models.bodyrequest_orders_actions_limit import BodyrequestOrdersActionsLimit
from swagger_client.models.bodyrequest_orders_actions_limit_instrument import BodyrequestOrdersActionsLimitInstrument
from swagger_client.models.bodyrequest_orders_actions_limit_tv import BodyrequestOrdersActionsLimitTV
from swagger_client.models.bodyrequest_orders_actions_limit_t_vput import BodyrequestOrdersActionsLimitTVput
from swagger_client.models.bodyrequest_orders_actions_limit_t_vput_instrument import BodyrequestOrdersActionsLimitTVputInstrument
from swagger_client.models.bodyrequest_orders_actions_limit_t_vput_user import BodyrequestOrdersActionsLimitTVputUser
from swagger_client.models.bodyrequest_orders_actions_limit_user import BodyrequestOrdersActionsLimitUser
from swagger_client.models.bodyrequest_orders_actions_market import BodyrequestOrdersActionsMarket
from swagger_client.models.bodyrequest_orders_actions_market_tv import BodyrequestOrdersActionsMarketTV
from swagger_client.models.bodyrequest_orders_actions_market_t_vput import BodyrequestOrdersActionsMarketTVput
from swagger_client.models.bodyrequest_orders_actions_stop import BodyrequestOrdersActionsStop
from swagger_client.models.bodyrequest_orders_actions_stop_instrument import BodyrequestOrdersActionsStopInstrument
from swagger_client.models.bodyrequest_orders_actions_stop_limit_tv import BodyrequestOrdersActionsStopLimitTV
from swagger_client.models.bodyrequest_orders_actions_stop_tv import BodyrequestOrdersActionsStopTV
from swagger_client.models.bodyrequest_orders_actions_stop_user import BodyrequestOrdersActionsStopUser
from swagger_client.models.bodyrequest_orders_actions_stoplimit import BodyrequestOrdersActionsStoplimit
from swagger_client.models.fortsrisk import Fortsrisk
from swagger_client.models.history import History
from swagger_client.models.history_object import HistoryObject
from swagger_client.models.inline_response400 import InlineResponse400
from swagger_client.models.money import Money
from swagger_client.models.order import Order
from swagger_client.models.orderbook import Orderbook
from swagger_client.models.orderbook_ask import OrderbookAsk
from swagger_client.models.orderbook_bid import OrderbookBid
from swagger_client.models.orders import Orders
from swagger_client.models.orders_actions400 import OrdersActions400
from swagger_client.models.orders_actions400_command_api import OrdersActions400CommandAPI
from swagger_client.models.orders_actions400_command_api_old_response import OrdersActions400CommandAPIOldResponse
from swagger_client.models.orders_actions_delete_order_id import OrdersActionsDeleteOrderId
from swagger_client.models.orders_actions_delete_order_id_command_api import OrdersActionsDeleteOrderIdCommandAPI
from swagger_client.models.orders_actions_limit_market import OrdersActionsLimitMarket
from swagger_client.models.orders_actions_limit_market_command_api import OrdersActionsLimitMarketCommandAPI
from swagger_client.models.orders_actions_stop_profit_loss import OrdersActionsStopProfitLoss
from swagger_client.models.orders_actions_stop_profit_loss_command_api import OrdersActionsStopProfitLossCommandAPI
from swagger_client.models.portfolio_info import PortfolioInfo
from swagger_client.models.portfolio_info_inner import PortfolioInfoInner
from swagger_client.models.position import Position
from swagger_client.models.positions import Positions
from swagger_client.models.risk import Risk
from swagger_client.models.securities import Securities
from swagger_client.models.security import Security
from swagger_client.models.servers_info import ServersInfo
from swagger_client.models.stoporder import Stoporder
from swagger_client.models.stoporders import Stoporders
from swagger_client.models.summary import Summary
from swagger_client.models.symbol import Symbol
from swagger_client.models.symbol_futures import SymbolFutures
from swagger_client.models.symbols import Symbols
from swagger_client.models.time import Time
from swagger_client.models.trade import Trade
from swagger_client.models.trades import Trades
