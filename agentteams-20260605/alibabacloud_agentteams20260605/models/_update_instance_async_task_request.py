# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceAsyncTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        is_resume: bool = None,
        task_code: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.is_resume = is_resume
        # This parameter is required.
        self.task_code = task_code
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_resume is not None:
            result['IsResume'] = self.is_resume

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsResume') is not None:
            self.is_resume = m.get('IsResume')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

