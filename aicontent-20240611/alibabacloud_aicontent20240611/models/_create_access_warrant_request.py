# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccessWarrantRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        request_sign: str = None,
        timestamp: str = None,
        user_client_ip: str = None,
        user_id: str = None,
        warrant_available: int = None,
    ):
        self.app_id = app_id
        self.request_sign = request_sign
        self.timestamp = timestamp
        self.user_client_ip = user_client_ip
        self.user_id = user_id
        self.warrant_available = warrant_available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.request_sign is not None:
            result['requestSign'] = self.request_sign

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.user_client_ip is not None:
            result['userClientIp'] = self.user_client_ip

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.warrant_available is not None:
            result['warrantAvailable'] = self.warrant_available

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('requestSign') is not None:
            self.request_sign = m.get('requestSign')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('userClientIp') is not None:
            self.user_client_ip = m.get('userClientIp')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('warrantAvailable') is not None:
            self.warrant_available = m.get('warrantAvailable')

        return self

