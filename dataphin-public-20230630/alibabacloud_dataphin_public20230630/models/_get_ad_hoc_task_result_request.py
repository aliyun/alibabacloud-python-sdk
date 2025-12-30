# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAdHocTaskResultRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        project_id: int = None,
        sub_task_id: int = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.sub_task_id = sub_task_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sub_task_id is not None:
            result['SubTaskId'] = self.sub_task_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubTaskId') is not None:
            self.sub_task_id = m.get('SubTaskId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

