# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        collaboration_group_id: str = None,
        definition_shrink: str = None,
        tenant_id: str = None,
    ):
        # The write action. Valid values: SAVE: Saves the template as a draft without taking effect. SUBMIT: Saves and submits the template and sets it as the only effective version. Default value: SUBMIT.
        self.action = action
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The complete JSON definition of the template, including name, description, and steps.
        # 
        # This parameter is required.
        self.definition_shrink = definition_shrink
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.definition_shrink is not None:
            result['definition'] = self.definition_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('definition') is not None:
            self.definition_shrink = m.get('definition')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

