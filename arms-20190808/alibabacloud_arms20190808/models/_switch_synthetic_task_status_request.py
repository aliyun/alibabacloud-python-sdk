# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SwitchSyntheticTaskStatusRequest(DaraModel):
    def __init__(
        self,
        switch_status: int = None,
        task_ids: List[int] = None,
    ):
        # Specifies whether to start or stop the task. Valid values:
        # 
        # *   **0**: stops the task
        # *   **1**: starts the task
        self.switch_status = switch_status
        # The task IDs. You can specify up to 30 task IDs at a time.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

