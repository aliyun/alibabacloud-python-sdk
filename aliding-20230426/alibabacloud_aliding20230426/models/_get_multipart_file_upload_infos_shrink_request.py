# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMultipartFileUploadInfosShrinkRequest(DaraModel):
    def __init__(
        self,
        option_shrink: str = None,
        part_numbers_shrink: str = None,
        tenant_context_shrink: str = None,
        upload_key: str = None,
    ):
        self.option_shrink = option_shrink
        self.part_numbers_shrink = part_numbers_shrink
        self.tenant_context_shrink = tenant_context_shrink
        self.upload_key = upload_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_shrink is not None:
            result['Option'] = self.option_shrink

        if self.part_numbers_shrink is not None:
            result['PartNumbers'] = self.part_numbers_shrink

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.upload_key is not None:
            result['UploadKey'] = self.upload_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            self.option_shrink = m.get('Option')

        if m.get('PartNumbers') is not None:
            self.part_numbers_shrink = m.get('PartNumbers')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('UploadKey') is not None:
            self.upload_key = m.get('UploadKey')

        return self

