# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScenegroupResponseBody(DaraModel):
    def __init__(
        self,
        open_conversation_id: str = None,
        request_id: str = None,
    ):
        self.open_conversation_id = open_conversation_id
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

