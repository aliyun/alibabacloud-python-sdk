# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetTaskStatus(DaraModel):
    def __init__(
        self,
        last_succeeded_time: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The time of the last completion.
        self.last_succeeded_time = last_succeeded_time
        # The start time of the task.
        self.start_time = start_time
        # The status of the task.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_succeeded_time is not None:
            result['LastSucceededTime'] = self.last_succeeded_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastSucceededTime') is not None:
            self.last_succeeded_time = m.get('LastSucceededTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

