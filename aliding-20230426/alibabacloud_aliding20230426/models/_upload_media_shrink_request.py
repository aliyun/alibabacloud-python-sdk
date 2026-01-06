# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMediaShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        media_name: str = None,
        media_type: str = None,
        org_id: int = None,
        url: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.media_name = media_name
        # This parameter is required.
        self.media_type = media_type
        # This parameter is required.
        self.org_id = org_id
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.media_name is not None:
            result['mediaName'] = self.media_name

        if self.media_type is not None:
            result['mediaType'] = self.media_type

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('mediaName') is not None:
            self.media_name = m.get('mediaName')

        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

