# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteExecutionsRequest(DaraModel):
    def __init__(
        self,
        execution_ids: str = None,
        force: bool = None,
        region_id: str = None,
    ):
        # The execution IDs.
        # 
        # You can specify multiple execution IDs in a JSON array in the format of `["xxxxxxxxx", "yyyyyyyyy", ... "zzzzzzzzz"]`. You can specify up to 100 execution IDs at a time. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.execution_ids = execution_ids
        # Whether to force delete the running task, the default value is false.
        self.force = force
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_ids is not None:
            result['ExecutionIds'] = self.execution_ids

        if self.force is not None:
            result['Force'] = self.force

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionIds') is not None:
            self.execution_ids = m.get('ExecutionIds')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

