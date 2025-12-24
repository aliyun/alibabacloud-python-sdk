# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlarmResponseBody(DaraModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the event-triggered task.
        self.alarm_task_id = alarm_task_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

