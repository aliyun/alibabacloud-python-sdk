# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerunWorkflowNodeRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        collaboration_group_id: str = None,
        node_key: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        plan_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The key of the starting node for the rerun, which includes fixed planning nodes and business execution nodes.
        # 
        # This parameter is required.
        self.node_key = node_key
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The current physical plan ID after the rerun. Rerunning a fixed planning node may generate a new plan. Use this value for subsequent queries.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The tenant ID. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.node_key is not None:
            result['nodeKey'] = self.node_key

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('nodeKey') is not None:
            self.node_key = m.get('nodeKey')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

