# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddFolderRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        option: main_models.AddFolderRequestOption = None,
        parent_id: str = None,
        space_id: str = None,
        tenant_context: main_models.AddFolderRequestTenantContext = None,
    ):
        # This parameter is required.
        self.name = name
        self.option = option
        # This parameter is required.
        self.parent_id = parent_id
        # This parameter is required.
        self.space_id = space_id
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

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Option') is not None:
            temp_model = main_models.AddFolderRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.AddFolderRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class AddFolderRequestTenantContext(DaraModel):
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

class AddFolderRequestOption(DaraModel):
    def __init__(
        self,
        app_properties: List[main_models.AddFolderRequestOptionAppProperties] = None,
        conflict_strategy: str = None,
    ):
        self.app_properties = app_properties
        self.conflict_strategy = conflict_strategy

    def validate(self):
        if self.app_properties:
            for v1 in self.app_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppProperties'] = []
        if self.app_properties is not None:
            for k1 in self.app_properties:
                result['AppProperties'].append(k1.to_map() if k1 else None)

        if self.conflict_strategy is not None:
            result['ConflictStrategy'] = self.conflict_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_properties = []
        if m.get('AppProperties') is not None:
            for k1 in m.get('AppProperties'):
                temp_model = main_models.AddFolderRequestOptionAppProperties()
                self.app_properties.append(temp_model.from_map(k1))

        if m.get('ConflictStrategy') is not None:
            self.conflict_strategy = m.get('ConflictStrategy')

        return self

class AddFolderRequestOptionAppProperties(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        visibility: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value
        # This parameter is required.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

