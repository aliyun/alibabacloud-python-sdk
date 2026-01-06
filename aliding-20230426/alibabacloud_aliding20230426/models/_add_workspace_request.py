# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddWorkspaceRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        option: main_models.AddWorkspaceRequestOption = None,
        tenant_context: main_models.AddWorkspaceRequestTenantContext = None,
    ):
        # This parameter is required.
        self.name = name
        self.option = option
        self.tenant_context = tenant_context

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
        if self.name is not None:
            result['Name'] = self.name

        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Option') is not None:
            temp_model = main_models.AddWorkspaceRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('TenantContext') is not None:
            temp_model = main_models.AddWorkspaceRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class AddWorkspaceRequestTenantContext(DaraModel):
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

class AddWorkspaceRequestOption(DaraModel):
    def __init__(
        self,
        description: str = None,
        team_id: str = None,
    ):
        self.description = description
        self.team_id = team_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.team_id is not None:
            result['TeamId'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('TeamId') is not None:
            self.team_id = m.get('TeamId')

        return self

