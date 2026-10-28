# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ViewOncallScheduleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schedule: Dict[str, List[main_models.ScheduleValue]] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The on-call calendar. The key is the shift name, and the value is a list of on-call shifts for the shift within the queried date range.
        self.schedule = schedule

    def validate(self):
        if self.schedule:
            for v1 in self.schedule.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['schedule'] = {}
        if self.schedule is not None:
            for k1, v1 in self.schedule.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['schedule'][k1] = l1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.schedule = {}
        if m.get('schedule') is not None:
            for k1, v1 in m.get('schedule').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ScheduleValue()
                    l1.append(temp_model.from_map(k2))
                self.schedule[k1] = l1

        return self

