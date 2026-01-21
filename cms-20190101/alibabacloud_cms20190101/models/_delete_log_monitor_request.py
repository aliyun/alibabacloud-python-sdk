# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogMonitorRequest(DaraModel):
    def __init__(
        self,
        log_id: int = None,
        region_id: str = None,
    ):
        # The ID of the log monitoring metric.
        # 
        # This parameter is required.
        self.log_id = log_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

