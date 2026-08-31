# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPhysicalNodeOperationLogRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        node_id: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The environment identifier. Valid values:
        # - DEV: development environment. 
        # - PROD (default): production environment.
        self.env = env
        # The node ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

