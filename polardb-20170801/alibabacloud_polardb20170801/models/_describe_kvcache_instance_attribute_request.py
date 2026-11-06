# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKVCacheInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        kvcache_instance_id: str = None,
    ):
        # The ID of the KVCache instance.
        # 
        # This parameter is required.
        self.kvcache_instance_id = kvcache_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kvcache_instance_id is not None:
            result['KVCacheInstanceId'] = self.kvcache_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KVCacheInstanceId') is not None:
            self.kvcache_instance_id = m.get('KVCacheInstanceId')

        return self

