# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceDocRequest(DaraModel):
    def __init__(
        self,
        doc_type: str = None,
        name: str = None,
        parent_node_id: str = None,
        template_id: str = None,
        template_type: str = None,
        tenant_context: main_models.CreateWorkspaceDocRequestTenantContext = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.doc_type = doc_type
        # This parameter is required.
        self.name = name
        self.parent_node_id = parent_node_id
        self.template_id = template_id
        self.template_type = template_type
        self.tenant_context = tenant_context
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

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

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

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
            temp_model = main_models.CreateWorkspaceDocRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateWorkspaceDocRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

