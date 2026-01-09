# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SuspendOutboundTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        outbound_task_id: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.outbound_task_id = outbound_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')

        return self

