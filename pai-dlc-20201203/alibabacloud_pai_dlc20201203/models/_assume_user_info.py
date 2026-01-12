# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssumeUserInfo(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        id: str = None,
        security_token: str = None,
        type: str = None,
    ):
        self.access_key_id = access_key_id
        self.id = id
        self.security_token = security_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.id is not None:
            result['Id'] = self.id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

