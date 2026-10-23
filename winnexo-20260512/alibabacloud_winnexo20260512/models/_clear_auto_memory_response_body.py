# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearAutoMemoryResponseBody(DaraModel):
    def __init__(
        self,
        cleared_count: int = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # The number of automatic memory files successfully deleted in this request. The value is 0 if no memory is available to be cleared.
        self.cleared_count = cleared_count
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The error description.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The type of automatic memory cleared in this request. Valid values: user, feedback, reference, project, and all.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cleared_count is not None:
            result['clearedCount'] = self.cleared_count

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clearedCount') is not None:
            self.cleared_count = m.get('clearedCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

