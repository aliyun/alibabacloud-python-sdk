# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCloudRecordVideoPlayInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        conference_id: str = None,
        media_id: str = None,
        region_id: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.conference_id = conference_id
        # This parameter is required.
        self.media_id = media_id
        # This parameter is required.
        self.region_id = region_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

