# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTokenRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        nonce: str = None,
        request_time: str = None,
        signature: str = None,
        token_key: str = None,
        token_type: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.nonce = nonce
        # This parameter is required.
        self.request_time = request_time
        # This parameter is required.
        self.signature = signature
        self.token_key = token_key
        # This parameter is required.
        self.token_type = token_type

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

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        if self.signature is not None:
            result['signature'] = self.signature

        if self.token_key is not None:
            result['tokenKey'] = self.token_key

        if self.token_type is not None:
            result['tokenType'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('tokenKey') is not None:
            self.token_key = m.get('tokenKey')

        if m.get('tokenType') is not None:
            self.token_type = m.get('tokenType')

        return self

