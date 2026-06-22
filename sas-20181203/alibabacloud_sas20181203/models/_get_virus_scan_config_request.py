# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVirusScanConfigRequest(DaraModel):
    def __init__(
        self,
        task_type: str = None,
    ):
        # The task type. Valid values:
        # - **VIRUS_VUL_SCHEDULE_SCAN**: virus scan.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

