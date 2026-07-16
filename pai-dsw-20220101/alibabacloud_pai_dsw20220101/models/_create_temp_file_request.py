# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTempFileRequest(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        instance_id: str = None,
        name: str = None,
        prefix: str = None,
        task_id: str = None,
    ):
        self.capacity = capacity
        self.instance_id = instance_id
        self.name = name
        self.prefix = prefix
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

