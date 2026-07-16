# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailianmodelonchip20240816 import models as main_models
from darabonba.model import DaraModel

class GetTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTokenResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        nonce: str = None,
        request_ip: str = None,
        response_time: str = None,
        signature: str = None,
    ):
        self.app_id = app_id
        self.device_name = device_name
        self.nonce = nonce
        self.request_ip = request_ip
        self.response_time = response_time
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.device_name is not None:
            result['deviceName'] = self.device_name

        if self.nonce is not None:
            result['nonce'] = self.nonce

        if self.request_ip is not None:
            result['requestIp'] = self.request_ip

        if self.response_time is not None:
            result['responseTime'] = self.response_time

        if self.signature is not None:
            result['signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')

        if m.get('requestIp') is not None:
            self.request_ip = m.get('requestIp')

        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        return self

