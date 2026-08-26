# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopLiveMPUTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: str = None,
    ):
        # The application ID. Only a single ID can be specified. The ID can contain uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters. You can view your application IDs by navigating to **ApsaraVideo Live > Live+ > ApsaraVideo Real-time Communication > Application Management**.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The task ID. Only a single ID can be specified. The ID can contain uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 55 characters. This ID serves as the identifier for the bypass forwarding task and must be unique.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

