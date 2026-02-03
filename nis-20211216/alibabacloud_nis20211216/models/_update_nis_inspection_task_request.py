# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNisInspectionTaskRequest(DaraModel):
    def __init__(
        self,
        inspection_task_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.inspection_task_id = inspection_task_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

