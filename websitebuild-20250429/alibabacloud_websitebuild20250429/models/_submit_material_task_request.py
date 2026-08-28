# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMaterialTaskRequest(DaraModel):
    def __init__(
        self,
        biz_group_id: str = None,
        task_param: str = None,
        task_type: str = None,
    ):
        # The business group ID.
        self.biz_group_id = biz_group_id
        # The task parameters.
        # 
        # This parameter is required.
        self.task_param = task_param
        # The task type.
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
        if self.biz_group_id is not None:
            result['BizGroupId'] = self.biz_group_id

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroupId') is not None:
            self.biz_group_id = m.get('BizGroupId')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

