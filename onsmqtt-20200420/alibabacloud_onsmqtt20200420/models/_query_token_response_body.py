# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        token_status: bool = None,
    ):
        # The unique ID that the system generates for the request. This parameter is a common parameter.
        self.request_id = request_id
        # The status of the queried token. Valid values:
        # 
        # *   **true**: indicates the token is valid.
        # *   **false**: indicates the token is invalid.
        self.token_status = token_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token_status is not None:
            result['TokenStatus'] = self.token_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TokenStatus') is not None:
            self.token_status = m.get('TokenStatus')

        return self

