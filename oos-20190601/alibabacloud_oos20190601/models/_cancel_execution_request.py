# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelExecutionRequest(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        region_id: str = None,
    ):
        # The ID of the execution.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

