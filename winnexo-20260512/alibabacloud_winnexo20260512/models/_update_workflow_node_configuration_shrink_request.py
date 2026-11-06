# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkflowNodeConfigurationShrinkRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        executor_shrink: str = None,
        expected_version: int = None,
        instance_id: str = None,
        model: str = None,
        node_id: str = None,
        responsible_user_ids_shrink: str = None,
        tenant_id: str = None,
    ):
        # 协作空间ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 节点执行人；省略保持，null恢复默认；与负责人、模型至少修改一项
        self.executor_shrink = executor_shrink
        # 读取接口返回的configVersion；非负整数；版本冲突须刷新
        # 
        # This parameter is required.
        self.expected_version = expected_version
        # 当前物理计划ID（planId）
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 模型模式；quick归一化standard；省略保持，null恢复默认
        self.model = model
        # 业务节点key（nodeKey）
        # 
        # This parameter is required.
        self.node_id = node_id
        # 节点负责人用户ID列表，非空正整数数组；省略保持，null恢复默认
        self.responsible_user_ids_shrink = responsible_user_ids_shrink
        # 租户ID；缺省使用调用方默认租户
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

        if self.responsible_user_ids_shrink is not None:
            result['responsibleUserIds'] = self.responsible_user_ids_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('responsibleUserIds') is not None:
            self.responsible_user_ids_shrink = m.get('responsibleUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

