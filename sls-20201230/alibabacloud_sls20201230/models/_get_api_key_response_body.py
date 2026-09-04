# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        allowed_stores: List[str] = None,
        api_key: str = None,
        api_key_name: str = None,
        create_time: int = None,
        description: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.allowed_stores = allowed_stores
        self.api_key = api_key
        self.api_key_name = api_key_name
        self.create_time = create_time
        self.description = description
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_stores is not None:
            result['allowedStores'] = self.allowed_stores

        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedStores') is not None:
            self.allowed_stores = m.get('allowedStores')

        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

