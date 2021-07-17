# coding: utf-8

"""
    Alor OpenAPI V2

    <small>Swagger-документация для API v1 доступна по ссылке&#58; <a href=\"https://alor.dev/rawdocs/WarpOpenApi3.yml\">https://alor.dev/rawdocs/WarpOpenApi3.yml</a></small><br><br> API для работы с торговой системой АЛОР Брокер. Предоставляет интерфейсы для выставления заявок и получения биржевой информации.  Данные для неавторизованных запросов предоставляются с 15-минутной задержкой, для авторизованных - без задержек.   Публичная биржевая информация может быть получена через HTTP(S) API, а также доступна через однократно установленное WebSocket соединение. <br> **Внимание!** WebSocket соединения могут и будут разрываться *(например, если клиент не успевает обрабатывать сообщения и на стороне API в буфере накопится более 5000 событий)*. <br> Во внешнем ПО необходимо предусмотреть механизмы переподключения и переподписки (при необходимости)! <br> <br>  В OpenAPI V2 \"Санкт-Петербургская биржа\" (SPBX) еще находится в процессе разработки. Доступно получение рыночных данных *(marketdata, md)*. Заявки на SPBX в V2 пока недоступны. В V1 торговый функционал для SPBX доступен.  <h4> Доступные типы данных </h4>  * Все сделки  * Все заявки  * Информация по инструментам  * Котировки  * Биржевые стаканы  * Исторические данные  * Позиции  * Информация о клиенте  <h4>Поддерживаемые виды заявок</h4>  * рыночные  * лимитные  * стоп-лосс  * тейк-профит  * стоп-лосс лимит  * тейк-профит лимит  <h4>    Ограничения по частоте запросов     </h4> <p>На текущий момент ограничений по количеству запросов в минуту или WebSocket-подписок нет. <br/> Сервер может обрабатывать \"тяжелые\" запросы (пример - история за все время) и запросы без авторизации с меньшим приоритетом. <br/> АЛОР оставляет за собой право на ограничение частоты запросов, если это будет необходимо для стабильной работы системы. <br/> <br/></p>   <h2> Авторизация </h2>  <h4>OAuth</h4>  <b>Внимание!</b>   JWT и refresh token — равносильны логину и паролю. Их нужно скрывать от публичного доступа.  <h4>Для разработчиков сторонних приложений, в которых торговлю будут вести их пользователи.</h4>  Мы предоставляем сервис для авторизации сторониих приложений по стандарту OAuth 2.0. С примером приложения, использующего OAuth сервис для авторизации пользователей можно ознакомиться в разделе  <a href=\"/examples\">Примеры</a>.  Список разрешений (scopes), которые могут быть выданы приложению: <table>   <tr>     <td><b>OrdersRead</b></td>     <td>Чтение выставленных заявок</td>   </tr>   <tr>     <td><b>OrdersCreate</b></td>     <td>Выставление заявок</td>   </tr>   <tr>     <td><b>Trades</b></td>     <td>Чтение совершенных сделок</td>   </tr>   <tr>     <td><b>Personal</b></td>     <td>Персональная информация: ФИО, почта и т.п.</td>   </tr>   <tr>     <td><b>Stats</b></td>     <td>Статистика: прибыль, средние цены и т.п.</td>   </tr> </table>  <h4>Для ведения операций от своего имени</h4>  Выписать себе <b>refresh token</b> для ведения операций от своего имени [можно здесь](https://alor.dev/open-api-tokens).  <h2>Краткое описание работы с авторизацией</h2>  Чтобы выполнить авторизованный запрос, добавьте в запрос заголовок с именем \"Authorization\" и значением, состоящим из префикса `\"Bearer \"` и валидного JWT токена.  Срок жизни JWT короткий: это сделано для безопасности.  Для большинства вариантов использования API мы рекоммендуем использовать механизм  <b>refresh token</b> .  Механизм  <b>refresh token</b>  позволяет получать JWT с новым сроком жизни. Для этого отправьте POST запрос на адрес `https://oauthdev.alor.ru/refresh?token={refreshToken}` *(игровой контур)* или `https://oauth.alor.ru/refresh?token={refreshToken}` *(боевой контур)*. Если у  <b>refresh token</b>  не истек срок жизни и не он не был отозван, то в теле ответа в поле AccessToken вернётся свежий JWT токен.   Срок жизни  <b>refresh token</b>, получаемого обычным способом — 1 месяц.   Срок жизни  <b>refresh token</b>, получаемого самостоятельным выписыванием — год.  | |-  > Если мы для вас не завели портфели для ведения торговли в игровом контуре, оставьте заявку на <a href=\"mailto:openapi@alor.ru\">openapi@alor.ru</a> или свяжитесь с нами в [телеграме](https://tgmssg.ru/AlorOpenAPI).  </br></br> Игровой контур: `https://apidev.alor.ru`  Боевой контур: `https://api.alor.ru`   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: openapi@alor.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BodyrequestOrdersActionsLimitTVput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'side': 'str',
        'type': 'str',
        'id': 'int',
        'quantity': 'int',
        'price': 'float',
        'instrument': 'BodyrequestOrdersActionsLimitTVputInstrument',
        'user': 'BodyrequestOrdersActionsLimitTVputUser'
    }

    attribute_map = {
        'side': 'side',
        'type': 'type',
        'id': 'id',
        'quantity': 'quantity',
        'price': 'price',
        'instrument': 'instrument',
        'user': 'user'
    }

    def __init__(self, side=None, type=None, id=None, quantity=None, price=None, instrument=None, user=None):  # noqa: E501
        """BodyrequestOrdersActionsLimitTVput - a model defined in Swagger"""  # noqa: E501
        self._side = None
        self._type = None
        self._id = None
        self._quantity = None
        self._price = None
        self._instrument = None
        self._user = None
        self.discriminator = None
        if side is not None:
            self.side = side
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if instrument is not None:
            self.instrument = instrument
        if user is not None:
            self.user = user

    @property
    def side(self):
        """Gets the side of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501

        Направление сделки. Купля либо продажа.  # noqa: E501

        :return: The side of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this BodyrequestOrdersActionsLimitTVput.

        Направление сделки. Купля либо продажа.  # noqa: E501

        :param side: The side of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: str
        """
        allowed_values = ["buy", "sell"]  # noqa: E501
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def type(self):
        """Gets the type of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501

        Тип заявки  # noqa: E501

        :return: The type of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BodyrequestOrdersActionsLimitTVput.

        Тип заявки  # noqa: E501

        :param type: The type of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501

        Идентификатор заявки  # noqa: E501

        :return: The id of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BodyrequestOrdersActionsLimitTVput.

        Идентификатор заявки  # noqa: E501

        :param id: The id of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def quantity(self):
        """Gets the quantity of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501

        Количество  # noqa: E501

        :return: The quantity of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this BodyrequestOrdersActionsLimitTVput.

        Количество  # noqa: E501

        :param quantity: The quantity of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501

        Цена  # noqa: E501

        :return: The price of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BodyrequestOrdersActionsLimitTVput.

        Цена  # noqa: E501

        :param price: The price of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def instrument(self):
        """Gets the instrument of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501


        :return: The instrument of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: BodyrequestOrdersActionsLimitTVputInstrument
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this BodyrequestOrdersActionsLimitTVput.


        :param instrument: The instrument of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: BodyrequestOrdersActionsLimitTVputInstrument
        """

        self._instrument = instrument

    @property
    def user(self):
        """Gets the user of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501


        :return: The user of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :rtype: BodyrequestOrdersActionsLimitTVputUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BodyrequestOrdersActionsLimitTVput.


        :param user: The user of this BodyrequestOrdersActionsLimitTVput.  # noqa: E501
        :type: BodyrequestOrdersActionsLimitTVputUser
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BodyrequestOrdersActionsLimitTVput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BodyrequestOrdersActionsLimitTVput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
