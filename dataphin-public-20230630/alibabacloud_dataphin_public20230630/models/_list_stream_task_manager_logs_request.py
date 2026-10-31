# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStreamTaskManagerLogsRequest(DaraModel):
    def __init__(
        self,
        deployment_instance_id: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
        taskmanager_id: str = None,
    ):
        # The ID of the Flink deployment instance.
        # 
        # This parameter is required.
        self.deployment_instance_id = deployment_instance_id
        # The ID of the operating tenant. The gateway verifies that the current identity has access to the tenant and then injects the TenantId into the backend.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The optional ID of the operator. This parameter follows the gateway identity verification rules and is not directly bound to the backend UserId.
        self.op_user_id = op_user_id
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The TaskManager ID. This parameter can be omitted when retrieving log content. If omitted, the JobManager logs are returned.
        # 
        # This parameter is required.
        self.taskmanager_id = taskmanager_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_instance_id is not None:
            result['DeploymentInstanceId'] = self.deployment_instance_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.taskmanager_id is not None:
            result['TaskmanagerId'] = self.taskmanager_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentInstanceId') is not None:
            self.deployment_instance_id = m.get('DeploymentInstanceId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TaskmanagerId') is not None:
            self.taskmanager_id = m.get('TaskmanagerId')

        return self

