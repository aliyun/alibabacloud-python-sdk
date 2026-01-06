# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConnectionResponseBody(DaraModel):
    def __init__(
        self,
        connection_id: str = None,
        request_id: str = None,
    ):
        # The connection ID.
        self.connection_id = connection_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

