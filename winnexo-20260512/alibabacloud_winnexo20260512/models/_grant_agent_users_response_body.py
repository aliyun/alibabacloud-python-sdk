# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantAgentUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        granted_count: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The number of authorization records processed in this request, including both newly created and updated records.
        self.granted_count = granted_count
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.granted_count is not None:
            result['grantedCount'] = self.granted_count

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('grantedCount') is not None:
            self.granted_count = m.get('grantedCount')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

