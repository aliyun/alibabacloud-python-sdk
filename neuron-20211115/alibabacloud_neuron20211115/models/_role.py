# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Role(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        enterprise_id: int = None,
        gmt_create: str = None,
        id: int = None,
        name: str = None,
        platform: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.enterprise_id = enterprise_id
        self.gmt_create = gmt_create
        self.id = id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.platform = platform
        self.request_id = request_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.platform is not None:
            result['platform'] = self.platform

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

