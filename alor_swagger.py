import swagger_client
import logging
from datetime import datetime

import hashlib
from json import JSONDecodeError
import requests

LOGGING = False
if LOGGING:
    logging.basicConfig(
        filename='debug.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.DEBUG
    )

TTL_JWT_TOKEN = 1740
URL_OAUTH = 'https://oauth.alor.ru'


class Api:
    @property
    def _random_order_id(self) -> str:
        data = self.username + str(datetime.timestamp(datetime.now()))
        rand_id = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return rand_id[:-30]

    def __init__(self, username=None, refresh=None):
        self.error = False
        self.username = username
        self.refresh_token = refresh
        self.token_ttl = TTL_JWT_TOKEN
        self.jwt_token = self._get_jwt_token()
        self.bearer = self._bearer()
        self.client = self.get_client()

    def get_client(self):
        self._bearer()
        client = swagger_client.api.default_api.DefaultApi(
            swagger_client.ApiClient(header_name='Authorization', header_value=self.bearer))
        self.client = client
        return client

    def _get_jwt_token(self):
        payload = {'token': self.refresh_token}
        res = requests.post(
            url=f'{URL_OAUTH}/refresh',
            params=payload
        )
        if res.status_code != 200:
            if LOGGING:
                logging.error(
                    f'Ошибка получения JWT токена: {res.status_code}')
            self.error = True
            return None
        try:
            token = res.json()
            jwt = token.get('AccessToken')
            self.token_ttl = int(datetime.timestamp(datetime.now()))
            return jwt
        except JSONDecodeError as e:
            self.error = True
            if LOGGING:
                logging.error(f'Ошибка декодирования JWT токена: {e}')
                return None

    def _bearer(self):
        now = int(datetime.timestamp(datetime.now()))
        if now - self.token_ttl > TTL_JWT_TOKEN:
            self.jwt_token = self._get_jwt_token()
        bearer = f"Bearer {self.jwt_token}"
        if not bearer:
            logging.error('Не найден JWT токен, запустите get_jwt()!')
            return None
        self.bearer = bearer
        return bearer
