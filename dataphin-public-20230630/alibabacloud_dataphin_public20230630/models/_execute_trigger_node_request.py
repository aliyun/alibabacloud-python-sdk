# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTriggerNodeRequest(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        env: str = None,
        index: int = None,
        node_id: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.biz_date = biz_date
        self.env = env
        self.index = index
        # This parameter is required.
        self.node_id = node_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.env is not None:
            result['Env'] = self.env

        if self.index is not None:
            result['Index'] = self.index

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

