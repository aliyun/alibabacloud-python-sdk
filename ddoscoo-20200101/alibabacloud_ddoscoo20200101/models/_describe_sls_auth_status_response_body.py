# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlsAuthStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_auth_status: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access Log Service. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sls_auth_status = sls_auth_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_auth_status is not None:
            result['SlsAuthStatus'] = self.sls_auth_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsAuthStatus') is not None:
            self.sls_auth_status = m.get('SlsAuthStatus')

        return self

