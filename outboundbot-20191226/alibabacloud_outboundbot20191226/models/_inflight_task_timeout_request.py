# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InflightTaskTimeoutRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_owner_id: int = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

