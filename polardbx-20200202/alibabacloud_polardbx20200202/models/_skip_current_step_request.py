# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkipCurrentStepRequest(DaraModel):
    def __init__(
        self,
        current_step: str = None,
        region_id: str = None,
        slink_task_id: str = None,
    ):
        self.current_step = current_step
        self.region_id = region_id
        self.slink_task_id = slink_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_step is not None:
            result['CurrentStep'] = self.current_step

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        return self

