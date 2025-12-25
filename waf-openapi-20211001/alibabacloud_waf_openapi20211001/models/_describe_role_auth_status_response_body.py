# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRoleAuthStatusResponseBody(DaraModel):
    def __init__(
        self,
        auth_status: bool = None,
        request_id: str = None,
    ):
        self.auth_status = auth_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

