# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTodoShrinkRequest(DaraModel):
    def __init__(
        self,
        assignee_user_ids_shrink: str = None,
        collaboration_group_id: str = None,
        priority: str = None,
        questions_shrink: str = None,
        source_context_shrink: str = None,
        source_type: str = None,
        tenant_id: str = None,
        title: str = None,
    ):
        # 处理人平台用户ID列表（1~100，去重后生效）
        # 
        # This parameter is required.
        self.assignee_user_ids_shrink = assignee_user_ids_shrink
        # 协作空间 ID（可选）
        self.collaboration_group_id = collaboration_group_id
        # 优先级
        self.priority = priority
        # 问题清单（1~N）
        # 
        # This parameter is required.
        self.questions_shrink = questions_shrink
        # 来源上下文（原样透传落库，不校验）
        # 
        # This parameter is required.
        self.source_context_shrink = source_context_shrink
        # 待办来源（仅 OPEN_API）
        # 
        # This parameter is required.
        self.source_type = source_type
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 待办标题（≤200 字）
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee_user_ids_shrink is not None:
            result['assigneeUserIds'] = self.assignee_user_ids_shrink

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.questions_shrink is not None:
            result['questions'] = self.questions_shrink

        if self.source_context_shrink is not None:
            result['sourceContext'] = self.source_context_shrink

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assigneeUserIds') is not None:
            self.assignee_user_ids_shrink = m.get('assigneeUserIds')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('questions') is not None:
            self.questions_shrink = m.get('questions')

        if m.get('sourceContext') is not None:
            self.source_context_shrink = m.get('sourceContext')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

