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
        # The batch action.
        # 
        # This parameter is required.
        self.action = action
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The idempotency key.
        # 
        # This parameter is required.
        self.idempotency_key = idempotency_key
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The IDs of the target work items. You can specify 1 to 100 IDs.
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

