# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertDropDownListShrinkRequest(DaraModel):
    def __init__(
        self,
        options_shrink: str = None,
        range_address: str = None,
        sheet_id: str = None,
        tenant_context_shrink: str = None,
        workbook_id: str = None,
    ):
        # This parameter is required.
        self.options_shrink = options_shrink
        # This parameter is required.
        self.range_address = range_address
        # This parameter is required.
        self.sheet_id = sheet_id
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.workbook_id = workbook_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.options_shrink is not None:
            result['Options'] = self.options_shrink

        if self.range_address is not None:
            result['RangeAddress'] = self.range_address

        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')

        if m.get('RangeAddress') is not None:
            self.range_address = m.get('RangeAddress')

        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')

        return self

