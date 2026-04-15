# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScencegroupFileDownloadurlShrinkRequest(DaraModel):
    def __init__(
        self,
        download_code: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.download_code = download_code
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_code is not None:
            result['DownloadCode'] = self.download_code

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadCode') is not None:
            self.download_code = m.get('DownloadCode')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

