# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertColumnsBeforeShrinkRequest(DaraModel):
    def __init__(
        self,
        column: int = None,
        column_count: int = None,
        sheet_id: str = None,
        tenant_context_shrink: str = None,
        workbook_id: str = None,
    ):
        # This parameter is required.
        self.column = column
        # This parameter is required.
        self.column_count = column_count
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
        if self.column is not None:
            result['Column'] = self.column

        if self.column_count is not None:
            result['ColumnCount'] = self.column_count

        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')

        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')

        return self

