# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRangeShrinkRequest(DaraModel):
    def __init__(
        self,
        background_colors_shrink: str = None,
        hyperlinks_shrink: str = None,
        number_format: str = None,
        range_address: str = None,
        sheet_id: str = None,
        tenant_context_shrink: str = None,
        values_shrink: str = None,
        workbook_id: str = None,
    ):
        self.background_colors_shrink = background_colors_shrink
        self.hyperlinks_shrink = hyperlinks_shrink
        self.number_format = number_format
        # This parameter is required.
        self.range_address = range_address
        # This parameter is required.
        self.sheet_id = sheet_id
        self.tenant_context_shrink = tenant_context_shrink
        self.values_shrink = values_shrink
        # This parameter is required.
        self.workbook_id = workbook_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_colors_shrink is not None:
            result['BackgroundColors'] = self.background_colors_shrink

        if self.hyperlinks_shrink is not None:
            result['Hyperlinks'] = self.hyperlinks_shrink

        if self.number_format is not None:
            result['NumberFormat'] = self.number_format

        if self.range_address is not None:
            result['RangeAddress'] = self.range_address

        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.values_shrink is not None:
            result['Values'] = self.values_shrink

        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundColors') is not None:
            self.background_colors_shrink = m.get('BackgroundColors')

        if m.get('Hyperlinks') is not None:
            self.hyperlinks_shrink = m.get('Hyperlinks')

        if m.get('NumberFormat') is not None:
            self.number_format = m.get('NumberFormat')

        if m.get('RangeAddress') is not None:
            self.range_address = m.get('RangeAddress')

        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('Values') is not None:
            self.values_shrink = m.get('Values')

        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')

        return self

