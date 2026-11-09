# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        # The common parameter. The ID of each request is unique.
        self.request_id = request_id
        # The token returned by the broker.
        # 
        # > Do not make any assumptions about the length, format, or rules of the returned token. The actual returned value prevails.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

