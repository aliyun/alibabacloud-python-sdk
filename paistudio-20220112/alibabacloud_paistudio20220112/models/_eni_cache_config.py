# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EniCacheConfig(DaraModel):
    def __init__(
        self,
        cache_pool_size: int = None,
        enabled: bool = None,
    ):
        self.cache_pool_size = cache_pool_size
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_pool_size is not None:
            result['CachePoolSize'] = self.cache_pool_size

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachePoolSize') is not None:
            self.cache_pool_size = m.get('CachePoolSize')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

