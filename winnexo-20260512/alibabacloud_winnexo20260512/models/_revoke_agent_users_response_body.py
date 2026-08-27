# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeAgentUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        revoked_count: int = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* / InvalidParameter.*).
        self.code = code
        # The error description. This is empty when the call succeeds.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The number of records successfully revoked in this call.
        self.revoked_count = revoked_count

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

        if self.revoked_count is not None:
            result['revokedCount'] = self.revoked_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('revokedCount') is not None:
            self.revoked_count = m.get('revokedCount')

        return self

