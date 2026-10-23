# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateWorkflowInstanceRequest(DaraModel):
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
        variables: Dict[str, Any] = None,
    ):
        # The required acceptance criteria for the workflow.
        # 
        # This parameter is required.
        self.acceptance_criteria = acceptance_criteria
        # The unique requirement ID in the workspace. Repeated requests are idempotent.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The display label of the external initiator.
        self.initiator = initiator
        # The work item priority.
        self.priority = priority
        # The workflow template ID. Maximum length: 64 characters.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The tenant ID. This is a common parameter explicitly passed by using --tenant-id in winnexo-cli.
        self.tenant_id = tenant_id
        # The requirement title.
        # 
        # This parameter is required.
        self.title = title
        # The business variable object. The tags field can be a list of string tags.
        self.variables = variables

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

        if self.variables is not None:
            result['variables'] = self.variables

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
            self.variables = m.get('variables')

        return self

