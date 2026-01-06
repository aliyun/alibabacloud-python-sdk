# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGroupLiveListShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        open_conversation_id: str = None,
        start_time: int = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.open_conversation_id = open_conversation_id
        # This parameter is required.
        self.start_time = start_time
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.open_conversation_id is not None:
            result['OpenConversationId'] = self.open_conversation_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OpenConversationId') is not None:
            self.open_conversation_id = m.get('OpenConversationId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

