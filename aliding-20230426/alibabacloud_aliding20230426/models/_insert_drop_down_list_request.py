# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class InsertDropDownListRequest(DaraModel):
    def __init__(
        self,
        options: List[main_models.InsertDropDownListRequestOptions] = None,
        range_address: str = None,
        sheet_id: str = None,
        tenant_context: main_models.InsertDropDownListRequestTenantContext = None,
        workbook_id: str = None,
    ):
        # This parameter is required.
        self.options = options
        # This parameter is required.
        self.range_address = range_address
        # This parameter is required.
        self.sheet_id = sheet_id
        self.tenant_context = tenant_context
        # This parameter is required.
        self.workbook_id = workbook_id

    def validate(self):
        if self.options:
            for v1 in self.options:
                 if v1:
                    v1.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['Options'].append(k1.to_map() if k1 else None)

        if self.range_address is not None:
            result['RangeAddress'] = self.range_address

        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.options = []
        if m.get('Options') is not None:
            for k1 in m.get('Options'):
                temp_model = main_models.InsertDropDownListRequestOptions()
                self.options.append(temp_model.from_map(k1))

        if m.get('RangeAddress') is not None:
            self.range_address = m.get('RangeAddress')

        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.InsertDropDownListRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')

        return self

class InsertDropDownListRequestTenantContext(DaraModel):
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

class InsertDropDownListRequestOptions(DaraModel):
    def __init__(
        self,
        color: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.color = color
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['Color'] = self.color

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

