# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMinutesTextShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        conference_id: str = None,
        direction: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.conference_id = conference_id
        # This parameter is required.
        self.direction = direction
        self.max_results = max_results
        self.next_token = next_token

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

        if self.direction is not None:
            result['direction'] = self.direction

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

