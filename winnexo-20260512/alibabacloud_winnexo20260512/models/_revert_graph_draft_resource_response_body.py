# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevertGraphDraftResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        reverted: bool = None,
    ):
        # The error code.
        self.code = code
        # The prompt message.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # Indicates whether the draft is actually revoked (true / false).
        # 
        # This parameter is required.
        self.reverted = reverted

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

        if self.reverted is not None:
            result['reverted'] = self.reverted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reverted') is not None:
            self.reverted = m.get('reverted')

        return self

