# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceActiveOpsTask(DaraModel):
    def __init__(
        self,
        instance_active_ops_task_id: str = None,
        instance_active_ops_task_status: str = None,
    ):
        self.instance_active_ops_task_id = instance_active_ops_task_id
        self.instance_active_ops_task_status = instance_active_ops_task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_active_ops_task_id is not None:
            result['InstanceActiveOpsTaskId'] = self.instance_active_ops_task_id

        if self.instance_active_ops_task_status is not None:
            result['InstanceActiveOpsTaskStatus'] = self.instance_active_ops_task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceActiveOpsTaskId') is not None:
            self.instance_active_ops_task_id = m.get('InstanceActiveOpsTaskId')

        if m.get('InstanceActiveOpsTaskStatus') is not None:
            self.instance_active_ops_task_status = m.get('InstanceActiveOpsTaskStatus')

        return self

