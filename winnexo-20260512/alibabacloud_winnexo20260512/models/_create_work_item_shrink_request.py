# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkItemShrinkRequest(DaraModel):
    def __init__(
        self,
        acceptance_criteria: str = None,
        attachments_shrink: str = None,
        collaboration_group_id: str = None,
        collaborator_user_ids_shrink: str = None,
        conversation_id: str = None,
        description: str = None,
        item_type: str = None,
        owner_user_id: int = None,
        priority: str = None,
        tenant_id: str = None,
        title: str = None,
        workflow_template_ids_shrink: str = None,
    ):
        # The acceptance criteria.
        self.acceptance_criteria = acceptance_criteria
        # The stable references of the input attachments.
        self.attachments_shrink = attachments_shrink
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The list of user IDs of the collaborators.
        self.collaborator_user_ids_shrink = collaborator_user_ids_shrink
        # The ID of the associated conversation.
        self.conversation_id = conversation_id
        # The description of the work item.
        self.description = description
        # The type of the work item. Only WORKFLOW is supported.
        # 
        # This parameter is required.
        self.item_type = item_type
        # The user ID of the owner. If this parameter is not specified, the ID of the caller is used.
        self.owner_user_id = owner_user_id
        # The scheduling priority.
        self.priority = priority
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The title of the work item.
        # 
        # This parameter is required.
        self.title = title
        # The list of IDs of the bound workflow templates.
        self.workflow_template_ids_shrink = workflow_template_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptance_criteria is not None:
            result['acceptanceCriteria'] = self.acceptance_criteria

        if self.attachments_shrink is not None:
            result['attachments'] = self.attachments_shrink

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.collaborator_user_ids_shrink is not None:
            result['collaboratorUserIds'] = self.collaborator_user_ids_shrink

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.description is not None:
            result['description'] = self.description

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        if self.workflow_template_ids_shrink is not None:
            result['workflowTemplateIds'] = self.workflow_template_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptanceCriteria') is not None:
            self.acceptance_criteria = m.get('acceptanceCriteria')

        if m.get('attachments') is not None:
            self.attachments_shrink = m.get('attachments')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('collaboratorUserIds') is not None:
            self.collaborator_user_ids_shrink = m.get('collaboratorUserIds')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('workflowTemplateIds') is not None:
            self.workflow_template_ids_shrink = m.get('workflowTemplateIds')

        return self

