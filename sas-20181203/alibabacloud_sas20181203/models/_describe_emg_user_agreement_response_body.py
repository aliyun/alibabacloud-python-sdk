# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEmgUserAgreementResponseBody(DaraModel):
    def __init__(
        self,
        auth: bool = None,
        request_id: str = None,
    ):
        # Indicates whether Security Center is authorized to scan for urgent vulnerabilities. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.auth = auth
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

