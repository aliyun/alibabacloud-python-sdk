# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddMultiDimTableRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        fields: List[main_models.AddMultiDimTableRequestFields] = None,
        name: str = None,
        tenant_context: main_models.AddMultiDimTableRequestTenantContext = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        self.fields = fields
        self.name = name
        self.tenant_context = tenant_context

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_id is not None:
            result['BaseId'] = self.base_id

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.AddMultiDimTableRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TenantContext') is not None:
            temp_model = main_models.AddMultiDimTableRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class AddMultiDimTableRequestTenantContext(DaraModel):
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

class AddMultiDimTableRequestFields(DaraModel):
    def __init__(
        self,
        name: str = None,
        property: Dict[str, Any] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.property = property
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.property is not None:
            result['Property'] = self.property

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

