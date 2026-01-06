# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMultiDimTableRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        record_ids_shrink: str = None,
        sheet_id_or_name: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        # This parameter is required.
        self.record_ids_shrink = record_ids_shrink
        # This parameter is required.
        self.sheet_id_or_name = sheet_id_or_name
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_id is not None:
            result['BaseId'] = self.base_id

        if self.record_ids_shrink is not None:
            result['RecordIds'] = self.record_ids_shrink

        if self.sheet_id_or_name is not None:
            result['SheetIdOrName'] = self.sheet_id_or_name

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        if m.get('RecordIds') is not None:
            self.record_ids_shrink = m.get('RecordIds')

        if m.get('SheetIdOrName') is not None:
            self.sheet_id_or_name = m.get('SheetIdOrName')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

