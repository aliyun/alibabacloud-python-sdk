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
        # The list of platform user IDs of the assignees. You can specify 1 to 100 IDs. Duplicate IDs are automatically removed.
        # 
        # This parameter is required.
        self.assignee_user_ids_shrink = assignee_user_ids_shrink
        # The ID of the collaboration workspace. This parameter is optional.
        self.collaboration_group_id = collaboration_group_id
        # The priority.
        self.priority = priority
        # The list of questions.
        # 
        # This parameter is required.
        self.questions_shrink = questions_shrink
        # The source context. The value is passed through and stored in the database as-is without validation.
        # 
        # This parameter is required.
        self.source_context_shrink = source_context_shrink
        # The source of the to-do item. Only OPEN_API is supported.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The title of the to-do item. The maximum length is 200 characters.
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

