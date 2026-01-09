# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncryptInvokeRequest(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        data: str = None,
        encrypt_key: str = None,
        method_name: str = None,
        sign: str = None,
    ):
        self.client_id = client_id
        self.data = data
        self.encrypt_key = encrypt_key
        self.method_name = method_name
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.data is not None:
            result['data'] = self.data

        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key

        if self.method_name is not None:
            result['methodName'] = self.method_name

        if self.sign is not None:
            result['sign'] = self.sign

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')

        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')

        if m.get('sign') is not None:
            self.sign = m.get('sign')

        return self

