# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ImportWorkflowTemplateRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        template: Dict[str, Any] = None,
        tenant_id: str = None,
    ):
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The portable template JSON. The stepId and sortOrder fields can be omitted.
        # 
        # This parameter is required.
        self.template = template
        # The tenant ID. This is a common parameter. If omitted, the default tenant of the caller is used.
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

        if self.template is not None:
            result['template'] = self.template

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('template') is not None:
            self.template = m.get('template')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

