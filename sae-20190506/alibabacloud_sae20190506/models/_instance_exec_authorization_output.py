# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceExecAuthorizationOutput(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        account_id: str = None,
        authorization: str = None,
        date: str = None,
        endpoint: str = None,
        request_id: str = None,
    ):
        self.access_key_id = access_key_id
        self.account_id = account_id
        self.authorization = authorization
        self.date = date
        self.endpoint = endpoint
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id

        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.authorization is not None:
            result['authorization'] = self.authorization

        if self.date is not None:
            result['date'] = self.date

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')

        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('authorization') is not None:
            self.authorization = m.get('authorization')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

