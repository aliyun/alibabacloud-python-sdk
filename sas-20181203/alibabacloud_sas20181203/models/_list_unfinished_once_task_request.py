# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUnfinishedOnceTaskRequest(DaraModel):
    def __init__(
        self,
        target: str = None,
        task_type: str = None,
    ):
        # The value of the object on which the task runs. If you set TaskType to IMAGE_SCAN, set this parameter to the UUID of the image that you want to scan. If you set TaskType to ASSETS_COLLECTION, set this parameter to the UUID of the server whose information you want to collect.
        self.target = target
        # The type of the task. Valid values:
        # 
        # *   **ASSETS_COLLECTION**: asset information collection task
        # *   **IMAGE_SCAN**: image scan task
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target is not None:
            result['Target'] = self.target

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

