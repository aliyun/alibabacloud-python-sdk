# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrafficControlTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_task_id: str = None,
    ):
        self.request_id = request_id
        self.traffic_control_task_id = traffic_control_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')

        return self

