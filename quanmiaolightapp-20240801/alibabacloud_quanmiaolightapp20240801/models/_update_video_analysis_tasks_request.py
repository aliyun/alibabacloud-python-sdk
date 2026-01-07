# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateVideoAnalysisTasksRequest(DaraModel):
    def __init__(
        self,
        task_ids: List[str] = None,
        task_status: str = None,
    ):
        # This parameter is required.
        self.task_ids = task_ids
        # This parameter is required.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

