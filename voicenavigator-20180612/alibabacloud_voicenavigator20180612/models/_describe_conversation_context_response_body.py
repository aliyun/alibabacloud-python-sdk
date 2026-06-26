# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConversationContextResponseBody(DaraModel):
    def __init__(
        self,
        conversation_context: str = None,
        request_id: str = None,
    ):
        # The conversation context, returned as a JSON string.
        self.conversation_context = conversation_context
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_context is not None:
            result['ConversationContext'] = self.conversation_context

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationContext') is not None:
            self.conversation_context = m.get('ConversationContext')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

