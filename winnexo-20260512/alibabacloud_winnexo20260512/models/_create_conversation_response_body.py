# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateConversationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        conversation_id: str = None,
        created_at: str = None,
        message: str = None,
        metadata: Dict[str, Any] = None,
        request_id: str = None,
        title: str = None,
    ):
        # The error code.
        self.code = code
        # Id of the request
        self.conversation_id = conversation_id
        # The time when the share was created.
        self.created_at = created_at
        # The status code description.
        self.message = message
        # A reserved field for extension use.
        self.metadata = metadata
        # The request ID.
        self.request_id = request_id
        # The appointment title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.message is not None:
            result['message'] = self.message

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

