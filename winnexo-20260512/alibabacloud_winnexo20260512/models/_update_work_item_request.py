# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkItemRequest(DaraModel):
    def __init__(
        self,
        acceptance_criteria: str = None,
        attachments: List[main_models.UpdateWorkItemRequestAttachments] = None,
        collaboration_group_id: str = None,
        collaborator_user_ids: List[int] = None,
        conversation_id: str = None,
        description: str = None,
        expected_version: int = None,
        owner_user_id: int = None,
        priority: str = None,
        tenant_id: str = None,
        title: str = None,
        work_item_id: str = None,
        workflow_template_ids: List[str] = None,
    ):
        # The acceptance criteria.
        self.acceptance_criteria = acceptance_criteria
        # The stable references for the attachments.
        self.attachments = attachments
        # The ID of the collaboration space.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The list of user IDs of the collaborators.
        self.collaborator_user_ids = collaborator_user_ids
        # The ID of the associated conversation.
        self.conversation_id = conversation_id
        # The description of the work item.
        self.description = description
        # The optimistic version number. Obtain this value from the version field in the previous response.
        # 
        # This parameter is required.
        self.expected_version = expected_version
        # The user ID of the owner. If not specified, the user ID of the caller is used.
        self.owner_user_id = owner_user_id
        # The scheduling priority.
        self.priority = priority
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The title of the work item.
        # 
        # This parameter is required.
        self.title = title
        # The ID of the work item.
        # 
        # This parameter is required.
        self.work_item_id = work_item_id
        # The list of bound workflow template IDs. If not specified, the existing bindings are retained. If an empty array is provided, the bindings are cleared.
        self.workflow_template_ids = workflow_template_ids

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptance_criteria is not None:
            result['acceptanceCriteria'] = self.acceptance_criteria

        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.collaborator_user_ids is not None:
            result['collaboratorUserIds'] = self.collaborator_user_ids

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.description is not None:
            result['description'] = self.description

        if self.expected_version is not None:
            result['expectedVersion'] = self.expected_version

        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        if self.workflow_template_ids is not None:
            result['workflowTemplateIds'] = self.workflow_template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptanceCriteria') is not None:
            self.acceptance_criteria = m.get('acceptanceCriteria')

        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.UpdateWorkItemRequestAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('collaboratorUserIds') is not None:
            self.collaborator_user_ids = m.get('collaboratorUserIds')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expectedVersion') is not None:
            self.expected_version = m.get('expectedVersion')

        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        if m.get('workflowTemplateIds') is not None:
            self.workflow_template_ids = m.get('workflowTemplateIds')

        return self

class UpdateWorkItemRequestAttachments(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        ref_url: str = None,
        resource_id: str = None,
        resource_kind: str = None,
        size_bytes: int = None,
        title: str = None,
    ):
        # The content type.
        self.content_type = content_type
        # The reference URL of the attachment.
        self.ref_url = ref_url
        # The resource ID of the attachment.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type of the attachment.
        # 
        # This parameter is required.
        self.resource_kind = resource_kind
        # The size of the attachment in bytes. The maximum size is 20 MB.
        self.size_bytes = size_bytes
        # The title of the attachment.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.ref_url is not None:
            result['refUrl'] = self.ref_url

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_kind is not None:
            result['resourceKind'] = self.resource_kind

        if self.size_bytes is not None:
            result['sizeBytes'] = self.size_bytes

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('refUrl') is not None:
            self.ref_url = m.get('refUrl')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceKind') is not None:
            self.resource_kind = m.get('resourceKind')

        if m.get('sizeBytes') is not None:
            self.size_bytes = m.get('sizeBytes')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

