# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMultiDimTableRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        filter_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        sheet_id_or_name: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        self.filter_shrink = filter_shrink
        self.max_results = max_results
        self.next_token = next_token
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

        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sheet_id_or_name is not None:
            result['SheetIdOrName'] = self.sheet_id_or_name

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SheetIdOrName') is not None:
            self.sheet_id_or_name = m.get('SheetIdOrName')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

