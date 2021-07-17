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

class Fortsrisk(object):
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
        'portfolio': 'str',
        'money_free': 'float',
        'money_blocked': 'float',
        'balance_money': 'float',
        'fee': 'float',
        'money_old': 'float',
        'money_amount': 'float',
        'money_pledge_amount': 'float',
        'vm_inter_cl': 'float',
        'vm_current_positions': 'float',
        'var_margin': 'float',
        'is_limits_set': 'bool'
    }

    attribute_map = {
        'portfolio': 'portfolio',
        'money_free': 'moneyFree',
        'money_blocked': 'moneyBlocked',
        'balance_money': 'balanceMoney',
        'fee': 'fee',
        'money_old': 'moneyOld',
        'money_amount': 'moneyAmount',
        'money_pledge_amount': 'moneyPledgeAmount',
        'vm_inter_cl': 'vmInterCl',
        'vm_current_positions': 'vmCurrentPositions',
        'var_margin': 'varMargin',
        'is_limits_set': 'isLimitsSet'
    }

    def __init__(self, portfolio=None, money_free=None, money_blocked=None, balance_money=None, fee=None, money_old=None, money_amount=None, money_pledge_amount=None, vm_inter_cl=None, vm_current_positions=None, var_margin=None, is_limits_set=None):  # noqa: E501
        """Fortsrisk - a model defined in Swagger"""  # noqa: E501
        self._portfolio = None
        self._money_free = None
        self._money_blocked = None
        self._balance_money = None
        self._fee = None
        self._money_old = None
        self._money_amount = None
        self._money_pledge_amount = None
        self._vm_inter_cl = None
        self._vm_current_positions = None
        self._var_margin = None
        self._is_limits_set = None
        self.discriminator = None
        if portfolio is not None:
            self.portfolio = portfolio
        if money_free is not None:
            self.money_free = money_free
        if money_blocked is not None:
            self.money_blocked = money_blocked
        if balance_money is not None:
            self.balance_money = balance_money
        if fee is not None:
            self.fee = fee
        if money_old is not None:
            self.money_old = money_old
        if money_amount is not None:
            self.money_amount = money_amount
        if money_pledge_amount is not None:
            self.money_pledge_amount = money_pledge_amount
        if vm_inter_cl is not None:
            self.vm_inter_cl = vm_inter_cl
        if vm_current_positions is not None:
            self.vm_current_positions = vm_current_positions
        if var_margin is not None:
            self.var_margin = var_margin
        if is_limits_set is not None:
            self.is_limits_set = is_limits_set

    @property
    def portfolio(self):
        """Gets the portfolio of this Fortsrisk.  # noqa: E501

        Идентификатор клиентского портфеля  # noqa: E501

        :return: The portfolio of this Fortsrisk.  # noqa: E501
        :rtype: str
        """
        return self._portfolio

    @portfolio.setter
    def portfolio(self, portfolio):
        """Sets the portfolio of this Fortsrisk.

        Идентификатор клиентского портфеля  # noqa: E501

        :param portfolio: The portfolio of this Fortsrisk.  # noqa: E501
        :type: str
        """

        self._portfolio = portfolio

    @property
    def money_free(self):
        """Gets the money_free of this Fortsrisk.  # noqa: E501

        Свободные средства. Сумма рублей и залогов, дисконтированных в рубли, доступная для открытия позиций. (MoneyFree = MoneyAmount + VmInterCl – MoneyBlocked – VmReserve – Fee)  # noqa: E501

        :return: The money_free of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._money_free

    @money_free.setter
    def money_free(self, money_free):
        """Sets the money_free of this Fortsrisk.

        Свободные средства. Сумма рублей и залогов, дисконтированных в рубли, доступная для открытия позиций. (MoneyFree = MoneyAmount + VmInterCl – MoneyBlocked – VmReserve – Fee)  # noqa: E501

        :param money_free: The money_free of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._money_free = money_free

    @property
    def money_blocked(self):
        """Gets the money_blocked of this Fortsrisk.  # noqa: E501

        Средства, заблокированные под ГО  # noqa: E501

        :return: The money_blocked of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._money_blocked

    @money_blocked.setter
    def money_blocked(self, money_blocked):
        """Sets the money_blocked of this Fortsrisk.

        Средства, заблокированные под ГО  # noqa: E501

        :param money_blocked: The money_blocked of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._money_blocked = money_blocked

    @property
    def balance_money(self):
        """Gets the balance_money of this Fortsrisk.  # noqa: E501

        Сальдо денежных торговых переводов за текущую сессию  # noqa: E501

        :return: The balance_money of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._balance_money

    @balance_money.setter
    def balance_money(self, balance_money):
        """Sets the balance_money of this Fortsrisk.

        Сальдо денежных торговых переводов за текущую сессию  # noqa: E501

        :param balance_money: The balance_money of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._balance_money = balance_money

    @property
    def fee(self):
        """Gets the fee of this Fortsrisk.  # noqa: E501

        Списанный сбор  # noqa: E501

        :return: The fee of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this Fortsrisk.

        Списанный сбор  # noqa: E501

        :param fee: The fee of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._fee = fee

    @property
    def money_old(self):
        """Gets the money_old of this Fortsrisk.  # noqa: E501

        Общее количество рублей и дисконтированных в рубли залогов на начало сессии  # noqa: E501

        :return: The money_old of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._money_old

    @money_old.setter
    def money_old(self, money_old):
        """Sets the money_old of this Fortsrisk.

        Общее количество рублей и дисконтированных в рубли залогов на начало сессии  # noqa: E501

        :param money_old: The money_old of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._money_old = money_old

    @property
    def money_amount(self):
        """Gets the money_amount of this Fortsrisk.  # noqa: E501

        Общее количество рублей и дисконтированных в рубли залогов  # noqa: E501

        :return: The money_amount of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._money_amount

    @money_amount.setter
    def money_amount(self, money_amount):
        """Sets the money_amount of this Fortsrisk.

        Общее количество рублей и дисконтированных в рубли залогов  # noqa: E501

        :param money_amount: The money_amount of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._money_amount = money_amount

    @property
    def money_pledge_amount(self):
        """Gets the money_pledge_amount of this Fortsrisk.  # noqa: E501

        Сумма залогов, дисконтированных в рубли  # noqa: E501

        :return: The money_pledge_amount of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._money_pledge_amount

    @money_pledge_amount.setter
    def money_pledge_amount(self, money_pledge_amount):
        """Sets the money_pledge_amount of this Fortsrisk.

        Сумма залогов, дисконтированных в рубли  # noqa: E501

        :param money_pledge_amount: The money_pledge_amount of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._money_pledge_amount = money_pledge_amount

    @property
    def vm_inter_cl(self):
        """Gets the vm_inter_cl of this Fortsrisk.  # noqa: E501

        Вариационная маржа, списанная или полученная в пром. клиринг  # noqa: E501

        :return: The vm_inter_cl of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._vm_inter_cl

    @vm_inter_cl.setter
    def vm_inter_cl(self, vm_inter_cl):
        """Sets the vm_inter_cl of this Fortsrisk.

        Вариационная маржа, списанная или полученная в пром. клиринг  # noqa: E501

        :param vm_inter_cl: The vm_inter_cl of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._vm_inter_cl = vm_inter_cl

    @property
    def vm_current_positions(self):
        """Gets the vm_current_positions of this Fortsrisk.  # noqa: E501

        Сагрегированная вармаржа по текущим позициям  # noqa: E501

        :return: The vm_current_positions of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._vm_current_positions

    @vm_current_positions.setter
    def vm_current_positions(self, vm_current_positions):
        """Sets the vm_current_positions of this Fortsrisk.

        Сагрегированная вармаржа по текущим позициям  # noqa: E501

        :param vm_current_positions: The vm_current_positions of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._vm_current_positions = vm_current_positions

    @property
    def var_margin(self):
        """Gets the var_margin of this Fortsrisk.  # noqa: E501

        VmCurrentPositions + VmInterCl  # noqa: E501

        :return: The var_margin of this Fortsrisk.  # noqa: E501
        :rtype: float
        """
        return self._var_margin

    @var_margin.setter
    def var_margin(self, var_margin):
        """Sets the var_margin of this Fortsrisk.

        VmCurrentPositions + VmInterCl  # noqa: E501

        :param var_margin: The var_margin of this Fortsrisk.  # noqa: E501
        :type: float
        """

        self._var_margin = var_margin

    @property
    def is_limits_set(self):
        """Gets the is_limits_set of this Fortsrisk.  # noqa: E501

        Наличие установленных денежного и залогового лимитов  # noqa: E501

        :return: The is_limits_set of this Fortsrisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_limits_set

    @is_limits_set.setter
    def is_limits_set(self, is_limits_set):
        """Sets the is_limits_set of this Fortsrisk.

        Наличие установленных денежного и залогового лимитов  # noqa: E501

        :param is_limits_set: The is_limits_set of this Fortsrisk.  # noqa: E501
        :type: bool
        """

        self._is_limits_set = is_limits_set

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
        if issubclass(Fortsrisk, dict):
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
        if not isinstance(other, Fortsrisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
