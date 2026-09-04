# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        api_keys: List[main_models.ListApiKeysResponseBodyApiKeys] = None,
        count: int = None,
        total: int = None,
    ):
        self.api_keys = api_keys
        self.count = count
        self.total = total

    def validate(self):
        if self.api_keys:
            for v1 in self.api_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiKeys'] = []
        if self.api_keys is not None:
            for k1 in self.api_keys:
                result['apiKeys'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['count'] = self.count

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_keys = []
        if m.get('apiKeys') is not None:
            for k1 in m.get('apiKeys'):
                temp_model = main_models.ListApiKeysResponseBodyApiKeys()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListApiKeysResponseBodyApiKeys(DaraModel):
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

