# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCacheReserveSpecificationResponseBody(DaraModel):
    def __init__(
        self,
        cache_reserve_capacity: List[str] = None,
        cache_reserve_region: List[str] = None,
        request_id: str = None,
    ):
        # List of cache retention capacity specifications.
        self.cache_reserve_capacity = cache_reserve_capacity
        # List of cache retention region specifications.
        self.cache_reserve_region = cache_reserve_region
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_reserve_capacity is not None:
            result['CacheReserveCapacity'] = self.cache_reserve_capacity

        if self.cache_reserve_region is not None:
            result['CacheReserveRegion'] = self.cache_reserve_region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheReserveCapacity') is not None:
            self.cache_reserve_capacity = m.get('CacheReserveCapacity')

        if m.get('CacheReserveRegion') is not None:
            self.cache_reserve_region = m.get('CacheReserveRegion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

