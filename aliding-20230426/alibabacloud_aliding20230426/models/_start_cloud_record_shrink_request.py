# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartCloudRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
        small_window_position: str = None,
        tenant_context_shrink: str = None,
        conference_id: str = None,
    ):
        self.mode = mode
        self.small_window_position = small_window_position
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.small_window_position is not None:
            result['SmallWindowPosition'] = self.small_window_position

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('SmallWindowPosition') is not None:
            self.small_window_position = m.get('SmallWindowPosition')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        return self

