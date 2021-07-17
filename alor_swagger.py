import hashlib
import logging
from datetime import datetime
from json import JSONDecodeError

import requests

import swagger_client

LOGGING = True  # Записывать ошибки в debug.log
DEVMODE = True  # в режиме разработчика, подключения идут к тествовым серверам
TTL_JWT_TOKEN = 1740  # Время жизни jwt-токена в секундах

if LOGGING:
    logging.basicConfig(
        filename="debug.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.DEBUG,
    )

URL_OAUTH = f'https://oauth{"dev" if DEVMODE else ""}.alor.ru'
URL_API = f'https://api{"dev" if DEVMODE else ""}.alor.ru'


class Api:
    @property
    def _random_order_id(self) -> str:
        data = self.username + str(datetime.timestamp(datetime.now()))
        rand_id = hashlib.sha256(data.encode("utf-8")).hexdigest()
        return rand_id[:-30]

    def __init__(self, username=None, refresh=None):
        self.error = False
        self.username = username
        self.refresh_token = refresh
        self.jwt_token = self._get_jwt_token()
        username_portfolios = self.client.dev_user_portfolio(username=self.username)

        self.fx_portfolio = username_portfolios['Валютный рынок'][0]['portfolio']
        self.fx_tks = username_portfolios['Валютный рынок'][0]['tks']
        self.fx_tradeServerCode = username_portfolios['Валютный рынок'][0]['tradeServersInfo'][0]['tradeServerCode']

        self.forts_portfolio = username_portfolios['Срочный рынок'][0]['portfolio']
        self.forts_tks = username_portfolios['Срочный рынок'][0]['tks']
        for server in username_portfolios['Срочный рынок'][0]['tradeServersInfo']:
            if server['contracts'] == 'фьючерсы':
                self.forts_futures_tradeServerCode = server['tradeServerCode']
            if server['contracts'] == 'опционы':
                self.forts_options_tradeServerCode = server['tradeServerCode']

        self.fund_portfolio = username_portfolios['Фондовый рынок'][0]['portfolio']
        self.fund_tks = username_portfolios['Фондовый рынок'][0]['tks']
        for server in username_portfolios['Фондовый рынок'][0]['tradeServersInfo']:
            if server['contracts'] == 'РЦБ':
                self.fund_moex_tradeServerCode = server['tradeServerCode']
            if server['contracts'] == 'ИЦБ':
                self.fund_spbx_tradeServerCode = server['tradeServerCode']

    def _get_jwt_token(self):
        payload = {"token": self.refresh_token}
        res = requests.post(url=f"{URL_OAUTH}/refresh", params=payload)
        if res.status_code != 200:
            if LOGGING:
                logging.error(f"Ошибка получения JWT токена: {res.status_code}")
            self.error = True
            return None
        try:
            token = res.json()
            jwt = token.get("AccessToken")
            self.jwt_token_issued_at = int(datetime.timestamp(datetime.now()))
            self.bearer = f"Bearer {jwt}"
            return jwt
        except JSONDecodeError as e:
            self.error = True
            if LOGGING:
                logging.error(f"Ошибка декодирования JWT токена: {e}")
                return None

    def _bearer(self):
        now = int(datetime.timestamp(datetime.now()))
        if now - self.jwt_token_issued_at > TTL_JWT_TOKEN:
            self.jwt_token = self._get_jwt_token()
        bearer = f"Bearer {self.jwt_token}"
        return self.bearer

    @property
    def client(self):
        self._bearer()
        swagger_client_conf = swagger_client.configuration.Configuration()
        swagger_client_conf.host = URL_API
        client = swagger_client.api.default_api.DefaultApi(
            swagger_client.ApiClient(configuration=swagger_client_conf,
                                     header_name="Authorization", header_value=self.bearer))
        return client
