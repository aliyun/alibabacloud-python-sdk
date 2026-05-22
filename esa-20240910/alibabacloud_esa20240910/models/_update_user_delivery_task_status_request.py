# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserDeliveryTaskStatusRequest(DaraModel):
    def __init__(
        self,
        method: str = None,
        task_name: str = None,
    ):
        # Enables or disables the delivery task. Valid values: online and offline.
        # 
        # This parameter is required.
        self.method = method
        # The name of the delivery task.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method is not None:
            result['Method'] = self.method

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

