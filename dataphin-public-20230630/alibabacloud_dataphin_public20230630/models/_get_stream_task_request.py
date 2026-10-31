# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStreamTaskRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
        task_id: str = None,
    ):
        # The environment to query. Valid values: DEV for the development environment, and PROD for the production environment. If this parameter is not specified, the gateway defaults to PROD. The value is case-insensitive.
        self.env = env
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id
        # The ID of the Dataphin project to which the task belongs. This parameter is used for project permission verification.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Instance ID of the real-time task instance. Instance ID starts with t_ and is not a node ID or a file ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

