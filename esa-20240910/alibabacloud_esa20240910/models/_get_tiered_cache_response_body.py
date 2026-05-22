# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTieredCacheResponseBody(DaraModel):
    def __init__(
        self,
        cache_architecture_mode: str = None,
        request_id: str = None,
    ):
        self.cache_architecture_mode = cache_architecture_mode
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_architecture_mode is not None:
            result['CacheArchitectureMode'] = self.cache_architecture_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheArchitectureMode') is not None:
            self.cache_architecture_mode = m.get('CacheArchitectureMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

