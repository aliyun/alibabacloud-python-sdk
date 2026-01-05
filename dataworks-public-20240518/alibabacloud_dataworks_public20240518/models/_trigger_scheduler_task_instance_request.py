# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerSchedulerTaskInstanceRequest(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        task_id: int = None,
        trigger_time: int = None,
    ):
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The time defined by the HTTP Trigger node. This value is a UNIX timestamp.
        # 
        # This parameter is required.
        self.trigger_time = trigger_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')

        return self

