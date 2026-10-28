# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteOncallSchedulesShrinkRequest(DaraModel):
    def __init__(
        self,
        oncall_schedule_ids_shrink: str = None,
    ):
        # The IDs of the on-call schedules.
        self.oncall_schedule_ids_shrink = oncall_schedule_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oncall_schedule_ids_shrink is not None:
            result['oncallScheduleIds'] = self.oncall_schedule_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oncallScheduleIds') is not None:
            self.oncall_schedule_ids_shrink = m.get('oncallScheduleIds')

        return self

