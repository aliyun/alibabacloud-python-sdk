# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteOncallSchedulesRequest(DaraModel):
    def __init__(
        self,
        oncall_schedule_ids: List[str] = None,
    ):
        self.oncall_schedule_ids = oncall_schedule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oncall_schedule_ids is not None:
            result['oncallScheduleIds'] = self.oncall_schedule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oncallScheduleIds') is not None:
            self.oncall_schedule_ids = m.get('oncallScheduleIds')

        return self

