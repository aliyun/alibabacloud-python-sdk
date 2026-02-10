# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetTaskResultRequest(DaraModel):
    def __init__(
        self,
        required_field_list: List[str] = None,
        task_id: str = None,
    ):
        self.required_field_list = required_field_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.required_field_list is not None:
            result['requiredFieldList'] = self.required_field_list

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredFieldList') is not None:
            self.required_field_list = m.get('requiredFieldList')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

