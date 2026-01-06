# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListMultiDimTableRecordsRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        filter: main_models.ListMultiDimTableRecordsRequestFilter = None,
        max_results: int = None,
        next_token: str = None,
        sheet_id_or_name: str = None,
        tenant_context: main_models.ListMultiDimTableRecordsRequestTenantContext = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.sheet_id_or_name = sheet_id_or_name
        self.tenant_context = tenant_context

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_id is not None:
            result['BaseId'] = self.base_id

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sheet_id_or_name is not None:
            result['SheetIdOrName'] = self.sheet_id_or_name

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        if m.get('Filter') is not None:
            temp_model = main_models.ListMultiDimTableRecordsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SheetIdOrName') is not None:
            self.sheet_id_or_name = m.get('SheetIdOrName')

        if m.get('TenantContext') is not None:
            temp_model = main_models.ListMultiDimTableRecordsRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class ListMultiDimTableRecordsRequestTenantContext(DaraModel):
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

class ListMultiDimTableRecordsRequestFilter(DaraModel):
    def __init__(
        self,
        combination: str = None,
        conditions: List[main_models.ListMultiDimTableRecordsRequestFilterConditions] = None,
    ):
        self.combination = combination
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.combination is not None:
            result['Combination'] = self.combination

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Combination') is not None:
            self.combination = m.get('Combination')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ListMultiDimTableRecordsRequestFilterConditions()
                self.conditions.append(temp_model.from_map(k1))

        return self

class ListMultiDimTableRecordsRequestFilterConditions(DaraModel):
    def __init__(
        self,
        field: str = None,
        operator: str = None,
        value: List[Any] = None,
    ):
        self.field = field
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

