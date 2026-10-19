# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchOperateWorkItemsShrinkRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        collaboration_group_id: str = None,
        idempotency_key: str = None,
        tenant_id: str = None,
        work_item_ids_shrink: str = None,
    ):
        # 批量动作
        # 
        # This parameter is required.
        self.action = action
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 幂等键
        # 
        # This parameter is required.
        self.idempotency_key = idempotency_key
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 目标工作项 ID 列表（1~100 个）
        # 
        # This parameter is required.
        self.work_item_ids_shrink = work_item_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.idempotency_key is not None:
            result['idempotencyKey'] = self.idempotency_key

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.work_item_ids_shrink is not None:
            result['workItemIds'] = self.work_item_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('idempotencyKey') is not None:
            self.idempotency_key = m.get('idempotencyKey')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workItemIds') is not None:
            self.work_item_ids_shrink = m.get('workItemIds')

        return self

