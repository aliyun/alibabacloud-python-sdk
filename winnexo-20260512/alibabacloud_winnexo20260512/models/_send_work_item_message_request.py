# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendWorkItemMessageRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        content: str = None,
        conversation_id: str = None,
        tenant_id: str = None,
        work_item_id: str = None,
    ):
        # The ID of the collaboration space.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The body of the user message. The value cannot be empty and can be up to 32,768 characters in length.
        # 
        # This parameter is required.
        self.content = content
        # The conversation ID returned by the API operation for creating a free exploration. You must specify at least one of this parameter and workItemId. If both are specified, they must match.
        self.conversation_id = conversation_id
        # The tenant ID. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The ID of the free exploration work item. This parameter is compatible with the legacy-topic:<conversationId> format. You must specify at least one of workItemId and conversationId. If both are specified, they must point to the same session.
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.content is not None:
            result['content'] = self.content

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

