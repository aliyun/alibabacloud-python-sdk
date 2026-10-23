# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CountTodosResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        pending_count: int = None,
        request_id: str = None,
        unread_count: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The error description.
        self.message = message
        # The number of pending items with the primary status of PENDING.
        self.pending_count = pending_count
        # The request tracking ID.
        self.request_id = request_id
        # The number of unread items where the readAt field of the handler is empty.
        self.unread_count = unread_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.unread_count is not None:
            result['unreadCount'] = self.unread_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('unreadCount') is not None:
            self.unread_count = m.get('unreadCount')

        return self

