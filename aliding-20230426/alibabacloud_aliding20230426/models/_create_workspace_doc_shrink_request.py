# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceDocShrinkRequest(DaraModel):
    def __init__(
        self,
        doc_type: str = None,
        name: str = None,
        parent_node_id: str = None,
        template_id: str = None,
        template_type: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.doc_type = doc_type
        # This parameter is required.
        self.name = name
        self.parent_node_id = parent_node_id
        self.template_id = template_id
        self.template_type = template_type
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

