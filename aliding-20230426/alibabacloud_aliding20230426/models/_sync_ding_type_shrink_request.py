# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncDingTypeShrinkRequest(DaraModel):
    def __init__(
        self,
        ding_type: str = None,
        is_dimission: str = None,
        source: str = None,
        tenant_context_shrink: str = None,
        work_no: str = None,
    ):
        # This parameter is required.
        self.ding_type = ding_type
        self.is_dimission = is_dimission
        # This parameter is required.
        self.source = source
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.work_no = work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding_type is not None:
            result['DingType'] = self.ding_type

        if self.is_dimission is not None:
            result['IsDimission'] = self.is_dimission

        if self.source is not None:
            result['Source'] = self.source

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.work_no is not None:
            result['WorkNo'] = self.work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingType') is not None:
            self.ding_type = m.get('DingType')

        if m.get('IsDimission') is not None:
            self.is_dimission = m.get('IsDimission')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WorkNo') is not None:
            self.work_no = m.get('WorkNo')

        return self

