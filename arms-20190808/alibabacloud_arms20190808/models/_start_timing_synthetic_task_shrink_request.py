# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartTimingSyntheticTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        task_ids_shrink: str = None,
    ):
        # The region ID. Default value: cn-hangzhou.
        self.region_id = region_id
        # The task IDs.
        self.task_ids_shrink = task_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_ids_shrink is not None:
            result['TaskIds'] = self.task_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskIds') is not None:
            self.task_ids_shrink = m.get('TaskIds')

        return self

