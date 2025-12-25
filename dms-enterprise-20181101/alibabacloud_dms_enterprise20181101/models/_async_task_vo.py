# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncTaskVO(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        id: int = None,
        remark: str = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        user_id: int = None,
    ):
        self.dataset_id = dataset_id
        self.id = id
        self.remark = remark
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.id is not None:
            result['Id'] = self.id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

