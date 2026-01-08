# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSlsLogDispatchRequest(DaraModel):
    def __init__(
        self,
        sls_region_id: str = None,
        ttl: int = None,
    ):
        # The region ID of the Simple Log Service project.
        self.sls_region_id = sls_region_id
        # The log retention period. Unit: days.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

