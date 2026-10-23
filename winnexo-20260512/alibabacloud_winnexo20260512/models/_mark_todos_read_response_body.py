# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MarkTodosReadResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        unread_count: int = None,
        updated_count: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The number of unread to-do items remaining after the operation.
        self.unread_count = unread_count
        # The number of to-do items marked as read in this request.
        self.updated_count = updated_count

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.unread_count is not None:
            result['unreadCount'] = self.unread_count

        if self.updated_count is not None:
            result['updatedCount'] = self.updated_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('unreadCount') is not None:
            self.unread_count = m.get('unreadCount')

        if m.get('updatedCount') is not None:
            self.updated_count = m.get('updatedCount')

        return self

