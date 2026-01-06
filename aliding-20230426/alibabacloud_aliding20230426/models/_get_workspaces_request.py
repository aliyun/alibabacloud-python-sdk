# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetWorkspacesRequest(DaraModel):
    def __init__(
        self,
        option: main_models.GetWorkspacesRequestOption = None,
        tenant_context: main_models.GetWorkspacesRequestTenantContext = None,
        workspace_ids: List[str] = None,
    ):
        self.option = option
        self.tenant_context = tenant_context
        # This parameter is required.
        self.workspace_ids = workspace_ids

    def validate(self):
        if self.option:
            self.option.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            temp_model = main_models.GetWorkspacesRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetWorkspacesRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')

        return self

class GetWorkspacesRequestTenantContext(DaraModel):
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

class GetWorkspacesRequestOption(DaraModel):
    def __init__(
        self,
        with_permission_role: bool = None,
    ):
        self.with_permission_role = with_permission_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_permission_role is not None:
            result['WithPermissionRole'] = self.with_permission_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WithPermissionRole') is not None:
            self.with_permission_role = m.get('WithPermissionRole')

        return self

