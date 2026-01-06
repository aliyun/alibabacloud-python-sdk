# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocContentTakIdShrinkRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        generate_cp: bool = None,
        target_format: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        self.generate_cp = generate_cp
        self.target_format = target_format
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

        if self.generate_cp is not None:
            result['GenerateCp'] = self.generate_cp

        if self.target_format is not None:
            result['TargetFormat'] = self.target_format

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('GenerateCp') is not None:
            self.generate_cp = m.get('GenerateCp')

        if m.get('TargetFormat') is not None:
            self.target_format = m.get('TargetFormat')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

