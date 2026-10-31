# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStreamOpsRecordsRequest(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
    ):
        # The ID of the real-time task file. The value is a string representing a positive integer.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the operation tenant. The gateway verifies that the current identity has access to the tenant and then injects the tenant ID into the backend.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The optional ID of the operator user. This parameter follows the gateway identity verification rules and is not directly bound to the backend user ID.
        self.op_user_id = op_user_id
        # The project ID.
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
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

