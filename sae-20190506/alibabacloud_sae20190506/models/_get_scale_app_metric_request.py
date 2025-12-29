# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScaleAppMetricRequest(DaraModel):
    def __init__(
        self,
        app_source: str = None,
        cpu_strategy: str = None,
        limit: int = None,
        region_id: str = None,
    ):
        # The SAE application type. Valid values:
        # 
        # *   **micro_service**
        # *   **web**
        # *   **job**
        self.app_source = app_source
        # The CPU allocation policy. Valid values:
        # 
        # *   **request**: CPU cores are allocated only when a request is initiated.
        # *   **always**: Fixed CPU cores are always allocated.
        self.cpu_strategy = cpu_strategy
        # The number of entries to return. Valid values: 0 to 100.
        # 
        # This parameter is required.
        self.limit = limit
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_source is not None:
            result['AppSource'] = self.app_source

        if self.cpu_strategy is not None:
            result['CpuStrategy'] = self.cpu_strategy

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSource') is not None:
            self.app_source = m.get('AppSource')

        if m.get('CpuStrategy') is not None:
            self.cpu_strategy = m.get('CpuStrategy')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

