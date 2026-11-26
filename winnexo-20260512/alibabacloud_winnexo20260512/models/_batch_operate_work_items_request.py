# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchOperateWorkItemsRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        app_token: str = None,
        collaboration_group_id: str = None,
        idempotency_key: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        work_item_ids: List[str] = None,
    ):
        # The batch action.
        # 
        # This parameter is required.
        self.action = action
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The idempotency key.
        # 
        # This parameter is required.
        self.idempotency_key = idempotency_key
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The IDs of the target work items. You can specify 1 to 100 IDs.
        # 
        # This parameter is required.
        self.work_item_ids = work_item_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.idempotency_key is not None:
            result['idempotencyKey'] = self.idempotency_key

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.work_item_ids is not None:
            result['workItemIds'] = self.work_item_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('idempotencyKey') is not None:
            self.idempotency_key = m.get('idempotencyKey')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workItemIds') is not None:
            self.work_item_ids = m.get('workItemIds')

        return self

