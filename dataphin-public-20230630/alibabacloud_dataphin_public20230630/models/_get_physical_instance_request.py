# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPhysicalInstanceRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        instance_id: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
    ):
        # Environment identifier.
        # DEV: Development environment.
        # PROD (default): Production environment.
        self.env = env
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Tenant ID
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # Project ID
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

