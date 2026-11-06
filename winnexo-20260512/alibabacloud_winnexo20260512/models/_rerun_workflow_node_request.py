# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerunWorkflowNodeRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        node_key: str = None,
        plan_id: str = None,
        tenant_id: str = None,
    ):
        # 协作空间ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 重跑起始节点 key，包含固定规划节点和业务执行节点
        # 
        # This parameter is required.
        self.node_key = node_key
        # 工作项当前物理计划ID
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # 租户ID，缺省使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.node_key is not None:
            result['nodeKey'] = self.node_key

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('nodeKey') is not None:
            self.node_key = m.get('nodeKey')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

