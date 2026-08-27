# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StreamChatMessageRequest(DaraModel):
    def __init__(
        self,
        last_event_id: str = None,
        tenant_id: str = None,
    ):
        # The last received SSE event ID, used for resuming delivery after a disconnection. If not specified, the full stream is replayed from the beginning.
        self.last_event_id = last_event_id
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_event_id is not None:
            result['lastEventId'] = self.last_event_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastEventId') is not None:
            self.last_event_id = m.get('lastEventId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

