# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSheetContentJobIdShrinkRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        export_type: str = None,
        tenant_context_shrink: str = None,
    ):
        self.dentry_uuid = dentry_uuid
        self.export_type = export_type
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

