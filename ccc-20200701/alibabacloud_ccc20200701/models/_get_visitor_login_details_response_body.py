# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetVisitorLoginDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetVisitorLoginDetailsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetVisitorLoginDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVisitorLoginDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        chat_app_id: str = None,
        chat_app_key: str = None,
        chat_device_id: str = None,
        chat_login_token: str = None,
        chat_server_url: str = None,
        chat_user_id: str = None,
    ):
        self.chat_app_id = chat_app_id
        self.chat_app_key = chat_app_key
        self.chat_device_id = chat_device_id
        self.chat_login_token = chat_login_token
        self.chat_server_url = chat_server_url
        self.chat_user_id = chat_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_app_id is not None:
            result['ChatAppId'] = self.chat_app_id

        if self.chat_app_key is not None:
            result['ChatAppKey'] = self.chat_app_key

        if self.chat_device_id is not None:
            result['ChatDeviceId'] = self.chat_device_id

        if self.chat_login_token is not None:
            result['ChatLoginToken'] = self.chat_login_token

        if self.chat_server_url is not None:
            result['ChatServerUrl'] = self.chat_server_url

        if self.chat_user_id is not None:
            result['ChatUserId'] = self.chat_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatAppId') is not None:
            self.chat_app_id = m.get('ChatAppId')

        if m.get('ChatAppKey') is not None:
            self.chat_app_key = m.get('ChatAppKey')

        if m.get('ChatDeviceId') is not None:
            self.chat_device_id = m.get('ChatDeviceId')

        if m.get('ChatLoginToken') is not None:
            self.chat_login_token = m.get('ChatLoginToken')

        if m.get('ChatServerUrl') is not None:
            self.chat_server_url = m.get('ChatServerUrl')

        if m.get('ChatUserId') is not None:
            self.chat_user_id = m.get('ChatUserId')

        return self

