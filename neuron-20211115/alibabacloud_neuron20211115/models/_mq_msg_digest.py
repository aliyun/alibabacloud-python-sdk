# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MqMsgDigest(DaraModel):
    def __init__(
        self,
        id: int = None,
        retry_count: int = None,
        store_size: int = None,
        store_time: str = None,
        tags: str = None,
    ):
        self.id = id
        self.retry_count = retry_count
        self.store_size = store_size
        self.store_time = store_time
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.store_size is not None:
            result['StoreSize'] = self.store_size

        if self.store_time is not None:
            result['StoreTime'] = self.store_time

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')

        if m.get('StoreTime') is not None:
            self.store_time = m.get('StoreTime')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

