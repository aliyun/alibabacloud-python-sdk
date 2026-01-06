# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateRangeRequest(DaraModel):
    def __init__(
        self,
        background_colors: List[List[str]] = None,
        hyperlinks: List[List[main_models.UpdateRangeRequestHyperlinks]] = None,
        number_format: str = None,
        range_address: str = None,
        sheet_id: str = None,
        tenant_context: main_models.UpdateRangeRequestTenantContext = None,
        values: List[List[str]] = None,
        workbook_id: str = None,
    ):
        self.background_colors = background_colors
        self.hyperlinks = hyperlinks
        self.number_format = number_format
        # This parameter is required.
        self.range_address = range_address
        # This parameter is required.
        self.sheet_id = sheet_id
        self.tenant_context = tenant_context
        self.values = values
        # This parameter is required.
        self.workbook_id = workbook_id

    def validate(self):
        if self.hyperlinks:
            for v1 in self.hyperlinks:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_colors is not None:
            result['BackgroundColors'] = self.background_colors

        result['Hyperlinks'] = []
        if self.hyperlinks is not None:
            for k1 in self.hyperlinks:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['Hyperlinks'].append(l1)

        if self.number_format is not None:
            result['NumberFormat'] = self.number_format

        if self.range_address is not None:
            result['RangeAddress'] = self.range_address

        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.values is not None:
            result['Values'] = self.values

        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundColors') is not None:
            self.background_colors = m.get('BackgroundColors')

        self.hyperlinks = []
        if m.get('Hyperlinks') is not None:
            for k1 in m.get('Hyperlinks'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.UpdateRangeRequestHyperlinks()
                    l1.append(temp_model.from_map(k2))
                self.hyperlinks.append(l1)

        if m.get('NumberFormat') is not None:
            self.number_format = m.get('NumberFormat')

        if m.get('RangeAddress') is not None:
            self.range_address = m.get('RangeAddress')

        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateRangeRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('Values') is not None:
            self.values = m.get('Values')

        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')

        return self

class UpdateRangeRequestTenantContext(DaraModel):
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

class UpdateRangeRequestHyperlinks(DaraModel):
    def __init__(
        self,
        type: str = None,
        link: str = None,
        text: str = None,
    ):
        self.type = type
        self.link = link
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.link is not None:
            result['Link'] = self.link

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

