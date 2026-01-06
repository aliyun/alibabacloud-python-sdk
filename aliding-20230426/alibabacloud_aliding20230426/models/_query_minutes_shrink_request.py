# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMinutesShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        conference_id: str = None,
    ):
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
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        return self

