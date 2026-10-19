# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        acceptance_criteria: str = None,
        business_id: str = None,
        collaboration_group_id: str = None,
        initiator: str = None,
        priority: str = None,
        template_id: str = None,
        tenant_id: str = None,
        title: str = None,
        variables_shrink: str = None,
    ):
        # Workflow 必填验收标准
        # 
        # This parameter is required.
        self.acceptance_criteria = acceptance_criteria
        # 空间内唯一需求编号，重复请求幂等
        # 
        # This parameter is required.
        self.business_id = business_id
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 外部发起人展示标签
        self.initiator = initiator
        # 工作项优先级
        self.priority = priority
        # 工作流模板 ID，最多 64 字符
        # 
        # This parameter is required.
        self.template_id = template_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id
        # 需求标题
        # 
        # This parameter is required.
        self.title = title
        # 业务变量对象，tags 可为字符串标签列表
        self.variables_shrink = variables_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptance_criteria is not None:
            result['acceptanceCriteria'] = self.acceptance_criteria

        if self.business_id is not None:
            result['businessId'] = self.business_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.initiator is not None:
            result['initiator'] = self.initiator

        if self.priority is not None:
            result['priority'] = self.priority

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        if self.variables_shrink is not None:
            result['variables'] = self.variables_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptanceCriteria') is not None:
            self.acceptance_criteria = m.get('acceptanceCriteria')

        if m.get('businessId') is not None:
            self.business_id = m.get('businessId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('variables') is not None:
            self.variables_shrink = m.get('variables')

        return self

