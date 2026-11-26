# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkflowNodeConfigurationShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        collaboration_group_id: str = None,
        executor_shrink: str = None,
        expected_version: int = None,
        instance_id: str = None,
        model: str = None,
        node_id: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        responsible_user_ids_shrink: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The executor of the node. If this parameter is omitted, the current value is retained. If this parameter is set to null, the default value is restored. You must modify at least one of the owner, model, or executor.
        self.executor_shrink = executor_shrink
        # The configuration version returned by the read operation. The value must be a non-negative integer. If a version conflict occurs, you must refresh the version.
        # 
        # This parameter is required.
        self.expected_version = expected_version
        # The ID of the current physical plan.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The model mode. The quick value is normalized to standard. If this parameter is omitted, the current value is retained. If this parameter is set to null, the default value is restored.
        self.model = model
        # The key of the business node.
        # 
        # This parameter is required.
        self.node_id = node_id
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The list of user IDs for the node owners. The value must be a non-empty array of positive integers. If this parameter is omitted, the current value is retained. If this parameter is set to null, the default value is restored.
        self.responsible_user_ids_shrink = responsible_user_ids_shrink
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

        if self.executor_shrink is not None:
            result['executor'] = self.executor_shrink

        if self.expected_version is not None:
            result['expectedVersion'] = self.expected_version

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.model is not None:
            result['model'] = self.model

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.responsible_user_ids_shrink is not None:
            result['responsibleUserIds'] = self.responsible_user_ids_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('executor') is not None:
            self.executor_shrink = m.get('executor')

        if m.get('expectedVersion') is not None:
            self.expected_version = m.get('expectedVersion')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('responsibleUserIds') is not None:
            self.responsible_user_ids_shrink = m.get('responsibleUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

