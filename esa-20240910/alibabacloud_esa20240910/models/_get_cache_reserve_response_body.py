# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCacheReserveResponseBody(DaraModel):
    def __init__(
        self,
        cache_reserve_instance_id: str = None,
        enable: str = None,
        request_id: str = None,
    ):
        # The cache reserve instance ID.
        self.cache_reserve_instance_id = cache_reserve_instance_id
        # The switch status. Valid values:
        # 
        # - **on**: Enabled.
        # - **off**: Disabled.
        self.enable = enable
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_reserve_instance_id is not None:
            result['CacheReserveInstanceId'] = self.cache_reserve_instance_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheReserveInstanceId') is not None:
            self.cache_reserve_instance_id = m.get('CacheReserveInstanceId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

